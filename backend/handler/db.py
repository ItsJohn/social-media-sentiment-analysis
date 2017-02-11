from bson import json_util
import json
import pymongo


client = pymongo.MongoClient()
db = client['tweetsDB']
collections = db['tweets']


def insert_data(data):
    for tweet in data:
        try:
            collections.insert_one(tweet)
        except Exception as e:
            e


def get_data_for_sentiment():
    return list(collections.find({
        'sentiment': {
            '$exists': False
        }
    }))


def insert_sentiment(tweetID, sentiment, confidence):
    collections.update({
        '_id': tweetID
    }, {
        '$set': {
            'sentiment': sentiment,
            'confidence': confidence
        }
    })


def format_time(tweets):
    new_tweets = []
    for tweet in tweets:
        tweet['timestamp'] = str(tweet['timestamp'])
        new_tweets.append(tweet)
    return new_tweets


def format_data(tweets):
    pos_count = 0
    neg_count = 0
    new_tweets = []
    for tweet in tweets:
        if '_id' in tweet:
            del tweet['_id']
        tweet['timestamp'] = str(tweet['timestamp'])
        if tweet['sentiment'] == 'positive':
            pos_count = pos_count + 1
        else:
            neg_count = neg_count + 1
        new_tweets.append(tweet)

    return {
        'total': pos_count + neg_count,
        'sentiment': {
            'positive': pos_count,
            'negative': neg_count
        },
        'tweets': new_tweets
    }


def get_keyword_tweets(term):
    return format_time(list(collections.find({
        'sentiment': {
            '$exists': True
        },
        'keyword': term,
        'confidence': 1
    }, {
        '_id': False
    })))


def get_keywords():
    keywords = list(collections.aggregate([{
        '$match': {
            'sentiment': {
                '$exists': True
            }
        }
    }, {
        '$group': {
            '_id': '$keyword'
        }
    }, {
        '$sort': {
            '_id': 1
        }
    }]))
    new_keywords = []
    for keyword in keywords:
        new_keywords.append(keyword['_id'])
    return new_keywords


def get_tweets_sentiments(term):
    return list(collections.find({
        'keyword': term,
        'sentiment': {
                '$exists': True
                }
    }, {
        'sentiment': 1,
        'confidence': 1,
        '_id': 0
    }
    ))


def retrieve_tweets(term):
    # sentiment = get_tweets_sentiments(term)
    tweets = get_keyword_tweets(term)
    return format_data(tweets)
