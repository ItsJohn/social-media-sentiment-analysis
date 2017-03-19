import tweepy.api
from tweepy import TweepError
from tweepy import AppAuthHandler
from tweepy import OAuthHandler

CKEY = "bhrii31PSB07bJAgMggvUXLck"
CSECRET = "rK4BCvXDFcfqrc0MuoUTzSTiQmj3FE2qJwyVZp91O84Es1oMz4"

SEARCH_CKEY = "3YV4NdxJ57eMGzTDsRAeoWzSW"
SEARCH_CSECRET = "DVKkEVnvmODm67ye4YVKXJmuPBuin99vukjOVPEsEfXAf26OnQ"


def appAuth():
    auth = AppAuthHandler(CKEY, CSECRET)
    api = tweepy.API(
        auth,
        wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True,
        parser=tweepy.parsers.JSONParser()
    )
    return api


def search_auth():
    auth = AppAuthHandler(SEARCH_CKEY, SEARCH_CSECRET)
    api = tweepy.API(
        auth,
        wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True,
        parser=tweepy.parsers.JSONParser()
    )
    return api


def query_twitter_for_tweets(
    word,
    since_id=None,
    max_id=None,
    use_since_id=False,
    auth=None
):
    new_tweets = []
    TWEET_PER_QUERY = 100
    if auth == 'search':
        auth = search_auth()
    else:
        auth = appAuth()

    try:
        if max_id is None:
            if since_id is None:
                new_tweets = auth.search(
                    q="'" + word + "' AND -filter:retweets",
                    count=TWEET_PER_QUERY,
                    lang="en",
                    include_entities=False
                )
        else:
            if since_id is None or not since_id or not use_since_id:
                new_tweets = auth.search(
                    q="'" + word + "' AND -filter:retweets",
                    count=TWEET_PER_QUERY,
                    max_id=max_id - 1,
                    lang="en",
                    include_entities=False
                )
            else:
                new_tweets = auth.search(
                    q="'" + word + "' AND -filter:retweets",
                    count=TWEET_PER_QUERY,
                    since_id=since_id,
                    lang="en",
                    include_entities=False
                )
    except TweepError as e:
        return e
    return new_tweets
