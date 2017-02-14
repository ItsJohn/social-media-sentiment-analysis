from datetime import datetime
from nltk.tokenize import TweetTokenizer
import re
import os.path


def extract_tweet(data, keyword):
    tweets = []

    for entry in data:
        tweets.append(strip_json_from_tweet(entry, keyword))

    return tweets


def strip_json_from_tweet(data, keyword):
    tweet = {}
    tweet['name'] = data['user']['name']
    tweet['text'] = remove_url(data['text'])
    tweet['timestamp'] = date_created(data['created_at'])
    tweet['favourite'] = data['favorite_count']
    tweet['retweet'] = data['retweet_count']
    tweet['keyword'] = keyword.lower()
    if data['coordinates']:
        tweet['coordinates'] = data['coordinates']['coordinates']

    return tweet


def date_created(date):
    date_time_format = datetime.strptime(date, '%a %b %d %X %z %Y')
    return date_time_format.replace(tzinfo=None)


def remove_url(text):
    # Twitter doesn't count the URL as part of the text
    # so it must be removed before inserting into the database
    return re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', text)
