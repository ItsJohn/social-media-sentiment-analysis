import handler.db as db

from datetime import datetime
import pymongo
import unittest


class DB_test(unittest.TestCase):

    def setUp(self):
        self.data = [{
            'text': 'This is a test',
            'sentiment': 'positive',
            'keyword': 'OpinionMiningTest',
            'platform': 'Twitter',
            'timestamp': str(datetime(2017, 1, 1, 1, 11, 11))
        }, {
            'text': 'This is another test',
            'sentiment': 'negative',
            'keyword': 'OpinionMiningTest',
            'platform': 'Facebook',
            'timestamp': str(datetime(2017, 2, 1, 1, 11, 11))
        }]

    def tearDown(self):
        client = pymongo.MongoClient()
        db = client['opinionMiningDB']
        collections = db['post']
        collections.delete_many({'keyword': 'OpinionMiningTest'})

    def test_insert_data(self):
        self.data[0]['confidence'] = 1
        self.data[1]['confidence'] = 1
        self.assertEqual(len(
            db.retrieve_keyword_post_without_platform('OpinionMiningTest')
        ), 0)
        db.insert_data(self.data)
        self.assertEqual(len(
            db.retrieve_keyword_post_without_platform('OpinionMiningTest')
        ), 2)

    def test_get_data_for_sentiment(self):
        new_data = [{
            'text': 'This is a new test',
            'keyword': 'OpinionMiningTest',
            'timestamp': str(datetime(2017, 2, 1, 1, 11, 11))
        }]
        self.assertEqual(len(db.get_data_for_sentiment()), 0)
        db.insert_data(new_data)
        self.assertEqual(len(db.get_data_for_sentiment()), 1)

    def test_insert_sentiment(self):
        new_data = [{
            'text': 'This is a new test',
            'keyword': 'OpinionMiningTest',
            'timestamp': str(datetime(2017, 2, 1, 1, 11, 11))
        }]
        db.insert_data(new_data)
        data = db.get_data_for_sentiment()
        self.assertEqual(len(data), 1)
        db.insert_sentiment(data[0]['_id'], 'positive', 0.2)
        self.assertEqual(len(db.get_data_for_sentiment()), 0)

    def test_retrieve_keyword_post_with_platform(self):
        self.data[0]['confidence'] = 1
        self.data[1]['confidence'] = 0.8
        formatted_data = [{
            'keyword': 'OpinionMiningTest',
            'text': 'This is a test',
            'timestamp': '2017-01-01 01:11:11',
            'confidence': 1,
            'sentiment': 'positive',
            'platform': 'Twitter'
        }]
        db.insert_data(self.data)
        self.assertEqual(
            db.retrieve_keyword_post_with_platform(
                'OpinionMiningTest',
                'Twitter'
            ),
            formatted_data
        )

    def test_retrieve_keyword_post_without_platform(self):
        self.data[0]['confidence'] = 1
        self.data[1]['confidence'] = 0.8
        formatted_data = [{
            'keyword': 'OpinionMiningTest',
            'platform': 'Twitter',
            'sentiment': 'positive',
            'timestamp': '2017-01-01 01:11:11',
            'text': 'This is a test',
            'confidence': 1
        }, {
            'keyword': 'OpinionMiningTest',
            'platform': 'Facebook',
            'sentiment': 'negative',
            'timestamp': '2017-02-01 01:11:11',
            'text': 'This is another test',
            'confidence': 0.8
        }]

        db.insert_data(self.data)
        self.assertEqual(
            db.retrieve_keyword_post_without_platform('OpinionMiningTest'),
            formatted_data
        )

    def test_retrieve_post(self):
        self.data[0]['confidence'] = 1
        formatted_data = [{
            'keyword': 'OpinionMiningTest',
            'text': 'This is a test',
            'timestamp': '2017-01-01 01:11:11',
            'platform': 'Twitter',
            'sentiment': 'positive',
            'confidence': 1
        }, {
            'sentiment': 'negative',
            'keyword': 'OpinionMiningTest',
            'text': 'This is another test',
            'timestamp': '2017-02-01 01:11:11',
            'platform': 'Facebook'
        }]
        db.insert_data(self.data)
        self.assertEqual(
            db.retrieve_post('OpinionMiningTest', 'All'),
            formatted_data
        )
        formatted_data = [{
            'timestamp': '2017-01-01 01:11:11',
            'platform': 'Twitter',
            'keyword': 'OpinionMiningTest',
            'text': 'This is a test',
            'sentiment': 'positive',
            'confidence': 1
        }]
        self.assertEqual(
            db.retrieve_post('OpinionMiningTest', 'Twitter'),
            formatted_data
        )
