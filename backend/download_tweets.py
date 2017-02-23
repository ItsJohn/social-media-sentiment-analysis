import sys
import pickle

from handler.utils.trends import load_trends_from_pickle
from handler.utils.trends import check_if_trends_already_exist
from handler.utils.curr_time import check_hour
from handler.utils.curr_time import check_minute
from handler.utils.curr_time import get_hour
from handler.utils.curr_time import get_minute
from handler.utils.tweet_utils import extract_tweet
from handler.utils.twitter_api import query_twitter_for_tweets
from handler.classifiers.sentiment import find_sentiment

from handler.slack import send_error_message
from handler.slack import send_report
from handler.db import insert_data

PICKLE_PATH = 'handler/utils/pickle/'
trends = load_trends_from_pickle()
time = {
    'hour': get_hour(),
    'minute': get_minute()
}


def set_pagination(tweets: list, trend: dict, index: int) -> dict:
    if len(tweets) != 0:
        if 'since_id' not in trend or tweets[0]['id'] > trend['since_id']:
            # since_id is the newest tweet
            trend['since_id'] = tweets[0]['id']
        if 'max_id' not in trend or tweets[-1]['id'] < trend['max_id']:
            # max_id is the oldest tweet
            trend['max_id'] = tweets[-1]['id']
    if 'use_since' in trend and trend['use_since'] and index == 0:
        # sets the current minute to check against if a half hour has passed
        # to check for new tweets
        time['minute'] = get_minute()
    trend['use_since'] = check_minute(time['minute'])
    return trend


def exit_program(error: str):
    with open(PICKLE_PATH + 'trends.pickle', 'wb') as ph:
        pickle.dump(trends, ph)
    send_error_message(error)


def download_tweet(trend: dict) -> dict:
    max_id = None
    since_id = None
    use_since = False
    if 'since_id' in trend and trend['since_id']:
        since_id = trend['since_id']
    if 'max_id' in trend and trend['max_id']:
        max_id = trend['max_id']
    if 'use_since' in trend:
        user_since = trend['use_since']

    new_tweets = query_twitter_for_tweets(
        trend['search_word'],
        since_id,
        max_id,
        use_since
    )
    return new_tweets


def retrieve_tweets(trends):
    index = 0
    loopIndex = 0

    while(True):
        if loopIndex is 450:
            print('Classifying tweets...')
            find_sentiment()
            loopIndex = 0
        new_tweets = download_tweet(trends[index])

        if type(new_tweets) is not dict:
            exit_program(str(new_tweets))

        trends[index] = set_pagination(
            new_tweets['statuses'],
            trends[index],
            index
        )

        # Process tweet
        new_tweets = extract_tweet(
            new_tweets['statuses'],
            trends[index]['formatted_word'])

        # Store Tweet
        insert_data(new_tweets)

        # Select next trend
        if check_hour(time['hour']):
            trends = check_if_trends_already_exist(trends)
            index = 0
        else:
            index = (index + 1) % len(trends)
        loopIndex = loopIndex + 1
        print(loopIndex, len(new_tweets), trends[index]['formatted_word'])


try:
    retrieve_tweets(trends)
except KeyboardInterrupt:
    exit_program('Someone broke me')
    sys.exit(0)
