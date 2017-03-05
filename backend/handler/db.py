from handler.db_utils import format_data
import json
import pymongo


client = pymongo.MongoClient()
db = client['opinionMiningDB']
collections = db['post']


def insert_data(data: str):
    for element in data:
        try:
            collections.insert_one(element)
        except Exception as e:
            e


def get_data_for_sentiment() -> list:
    """ Retrieves all post without a sentiment """
    return list(collections.find({
        'sentiment': {
            '$exists': False
        }
    }))


def insert_sentiment(postID: int, sentiment: str, confidence: float):
    collections.update_one({
        '_id': postID
    }, {
        '$set': {
            'sentiment': sentiment,
            'confidence': confidence
        }
    })


def retrieve_keyword_post_with_platform(term: str, platform: str) -> list:
    """ Retrieves post associated with a keyword
        with a sentiment with a specific platform"""
    return list(collections.find({
        'sentiment': {
            '$exists': True
        },
        'keyword': term,
        'platform': platform
    }, {
        '_id': False,
        'tweetID': False
    }))


def retrieve_keyword_post_without_platform(term: str) -> list:
    """ Retrieves post associated with a keyword
        with a sentiment with no specific platform """
    return list(collections.find({
        'sentiment': {
            '$exists': True
        },
        'keyword': term
    }, {
        '_id': False,
        'tweetID': False
    }))


def get_keywords() -> list:
    """ Retrieves Keywords with associated sentiments """
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


def retrieve_post(term: str, platform: str) -> dict:
    if platform == 'All':
        data = retrieve_keyword_post_without_platform(term)
    else:
        data = retrieve_keyword_post_with_platform(term, platform)
    return format_data(data)
