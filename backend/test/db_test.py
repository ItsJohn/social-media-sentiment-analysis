import handler.db as db

from datetime import datetime
import pymongo
import unittest


class DB_test(unittest.TestCase):

    def setUp(self):
        self.data = [{
            'text': 'This is a test',
            'sentiment': 'positive',
            'keyword': 'test',
            'timestamp': datetime(2017, 1, 1, 1, 11, 11, 387893)
        }, {
            'text': 'This is another test',
            'sentiment': 'negative',
            'keyword': 'test',
            'timestamp': datetime(2017, 2, 1, 1, 11, 11, 387893)
        }]

    def tearDown(self):
        client = pymongo.MongoClient()
        db = client['tweetsDB']
        collections = db['tweets']
        collections.delete_many({'keyword': 'test'})

    def test_insert_data(self):
        self.data[0]['confidence'] = 1
        self.data[1]['confidence'] = 1
        self.assertEqual(len(db.get_keyword_tweets('test')), 0)
        db.insert_data(self.data)
        self.assertEqual(len(db.get_keyword_tweets('test')), 2)

    def test_get_data_for_sentiment(self):
        new_data = [{
            'text': 'This is a new test',
            'keyword': 'test',
            'timestamp': datetime(2017, 2, 1, 1, 11, 11, 387893)
        }]
        self.assertEqual(len(db.get_data_for_sentiment()), 0)
        db.insert_data(new_data)
        self.assertEqual(len(db.get_data_for_sentiment()), 1)

    def test_insert_sentiment(self):
        new_data = [{
            'text': 'This is a new test',
            'keyword': 'test',
            'timestamp': datetime(2017, 2, 1, 1, 11, 11, 387893)
        }]
        db.insert_data(new_data)
        data = db.get_data_for_sentiment()
        self.assertEqual(len(data), 1)
        db.insert_sentiment(data[0]['_id'], 'positive', 0.2)
        self.assertEqual(len(db.get_data_for_sentiment()), 0)

    def test_format_time(self):
        formatted_date = [{
            'keyword': 'test',
            'text': 'This is a test',
            'sentiment': 'positive',
            'timestamp': '2017-01-01 01:11:11.387893'
        }, {
            'keyword': 'test',
            'text': 'This is another test',
            'sentiment': 'negative',
            'timestamp': '2017-02-01 01:11:11.387893'
        }]
        self.assertEqual(db.format_time(self.data), formatted_date)

    def test_format_data(self):
        formatted_data = {
            'tweets': [{
                'timestamp': '2017-01-01 01:11:11.387893',
                'sentiment': 'positive',
                'text': 'This is a test',
                'keyword': 'test'
            }, {
                'timestamp': '2017-02-01 01:11:11.387893',
                'sentiment': 'negative',
                'text': 'This is another test',
                'keyword': 'test'
            }],
            'coordinates': [],
            'sentiment': {
                'negative': 1,
                'positive': 1
            },
            'total': 2
        }
        self.assertEqual(db.format_data(self.data), formatted_data)

    def test_get_keyword_tweets(self):
        self.data[0]['confidence'] = 1
        self.data[1]['confidence'] = 0.8
        formatted_data = [{
            'timestamp': '2017-01-01 01:11:11.387000',
            'text': 'This is a test',
            'confidence': 1,
            'keyword': 'test',
            'sentiment': 'positive'
        }]
        db.insert_data(self.data)
        self.assertEqual(db.get_keyword_tweets('test'), formatted_data)

    def test_get_keywords(self):
        db.insert_data(self.data)
        self.assertEqual(db.get_keywords(), ['test'])

    def test_retrieve_tweets(self):
        self.data[0]['confidence'] = 1
        formatted_data = {
            'tweets': [{
                'confidence': 1,
                'timestamp': '2017-01-01 01:11:11.387000',
                'keyword': 'test',
                'text': 'This is a test',
                'sentiment': 'positive'
            }],
            'coordinates': [],
            'total': 1,
            'sentiment': {
                'positive': 1,
                'negative': 0
            }
        }
        db.insert_data(self.data)
        self.assertEqual(db.retrieve_tweets('test'), formatted_data)
