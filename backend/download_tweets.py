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

from handler.slack import send_error_message
from handler.slack import send_report
from handler.db import insert_data


trends = load_trends_from_pickle()
time = {
    'hour': get_hour(),
    'minute': get_minute()
}


def set_pagination(tweets, trend, index):
    if len(tweets['statuses']) != 0:
        if 'since_id' not in trend or tweets['statuses'][0]['id'] > trend['since_id']:
            trend['since_id'] = tweets['statuses'][0]['id']
        if 'max_id' not in trend or tweets['statuses'][-1]['id'] < trend['max_id']:
            trend['max_id'] = tweets['statuses'][-1]['id']
    if 'use_since' in trend and trend['use_since'] and index == 0:
        time['minute'] = get_minute()
    trends[index]['use_since'] = check_minute(time['minute'])


def exit_program(error):
    with open('pickle/trends.pickle', 'wb') as ph:
        pickle.dump(trends, ph)
    send_error_message(error)


def download_tweet(trend):
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
        loopIndex = loopIndex + 1
        # if loopIndex % 450 is 0:
        new_tweets = download_tweet(trends[index])

        if type(new_tweets) is not dict:
            exit_program(str(new_tweets))

        if check_hour(time['hour']):
            trends = check_if_trends_already_exist(trends)

        set_pagination(new_tweets, trends[index], index)

        # Process tweet
        new_tweets = extract_tweet(
            new_tweets['statuses'],
            trends[index]['formatted_word'])

        # Store Tweet
        insert_data(new_tweets)

        # Select next trend
        index = (index + 1) % len(trends)
        print(loopIndex, len(new_tweets))


try:
    retrieve_tweets(trends)
except KeyboardInterrupt:
    exit_program('Someone broke me')
    sys.exit(0)
