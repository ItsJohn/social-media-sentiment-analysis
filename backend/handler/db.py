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


def get_keyword_tweets(term):
    tweets = list(collections.find({
        'sentiment': {
            '$exists': True
        },
        'keyword': term,
        'confidence': 1
    }, {
        '_id': False
    }))
    new_tweets = []
    for tweet in tweets:
        tweet['timestamp'] = str(tweet['timestamp'])
        new_tweets.append(tweet)
    return new_tweets


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
    tweets = list(collections.find({
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
    pos_count = 0
    neg_count = 0
    for tweet in tweets:
        if tweet['sentiment'] == 'positive':
            pos_count = pos_count + 1
        else:
            neg_count = neg_count + 1

    return pos_count, neg_count


def retrieve_tweets(term):
    pos_count, neg_count = get_tweets_sentiments(term)
    return {
        'total': pos_count + neg_count,
        'sentiment': {
            'positive': pos_count,
            'negative': neg_count
        },
        'tweets': get_keyword_tweets(term)
    }
