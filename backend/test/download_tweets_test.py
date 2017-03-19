import platforms.twitter.download_tweets as dt

from time import gmtime
from os import remove
from unittest.mock import patch
import os.path
import unittest


class Download_Tweet_test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_set_pagination(self):
        # should only return 'use_since'
        self.assertEqual(dt.set_pagination([], {}, 0), {'use_since': False})
        # should return 'use_since' as well as 'since_id' and 'max_id'
        tweets = [{'id': 2}, {'id': 1}]
        formatted_data = {
            'use_since': False,
            'since_id': 2,
            'max_id': 1
        }
        self.assertEqual(dt.set_pagination(tweets, {}, 0), formatted_data)
        # shoud update 'since_id' to the new value
        trend = {
            'use_since': False,
            'since_id': 1,
            'max_id': 1
        }
        self.assertEqual(dt.set_pagination(tweets, trend, 0), formatted_data)
        # should update 'max_id'
        trend = {
            'use_since': False,
            'since_id': 2,
            'max_id': 2
        }
        self.assertEqual(dt.set_pagination(tweets, trend, 0), formatted_data)
        # should change 'use_since' to True
        dt.time['minute'] = gmtime().tm_min - 30
        formatted_data = {
            'use_since': True,
            'since_id': 2,
            'max_id': 1
        }
        self.assertEqual(dt.set_pagination(tweets, trend, 3), formatted_data)
        # should reset 'use_since' to False
        trend = {
            'use_since': True,
            'since_id': 2,
            'max_id': 1
        }
        formatted_data = {
            'use_since': False,
            'since_id': 2,
            'max_id': 1
        }
        self.assertEqual(dt.set_pagination(tweets, trend, 0), formatted_data)

    def test_exit_program(self):
        dt.PICKLE_PATH = 'test/mock/'
        dt.exit_program('oh oh', [])
        self.assertTrue(os.path.isfile(dt.PICKLE_PATH + 'trends.pickle'))
        remove(dt.PICKLE_PATH + 'trends.pickle')

    def test_download_tweet(self):
        trend = {
            'search_word': 'word'
        }
        self.assertEqual(len(dt.download_tweet(trend)), 2)
