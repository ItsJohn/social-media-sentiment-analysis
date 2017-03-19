# Platform dependent
# Twitter
from platforms.twitter.download_tweets import retrieve_tweets
from platforms.twitter.twitter_api import query_twitter_for_tweets
from platforms.twitter.tweet_utils import extract_tweet
from handler.classifiers.sentiment import classify_data


# TODO: Add new platform here
platforms = [
    'Twitter'
]


def download_continuously(chosen_platform: str):
    # TODO: Add platforms download here
    if chosen_platform == 'Twitter':
        retrieve_tweets()


def download_single_set_of_posts(term: str, platform: str) -> list:
    # TODO: Add an if statement for new platform, set data to formatted list
    if platform == 'Twitter':
        data = extract_tweet(
            query_twitter_for_tweets(term, auth='search')['statuses'],
            term
        )
    else:
        # Default download from Twitter
        data = extract_tweet(
            query_twitter_for_tweets(term, auth='search')['statuses'],
            term
        )
    return data
