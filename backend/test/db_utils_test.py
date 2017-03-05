from handler.db_utils import format_data

from datetime import datetime
import unittest


class DB_utils_test(unittest.TestCase):

    def test_format_data(self):
        data = [{
            'text': 'This is a test',
            'sentiment': 'positive',
            'keyword': 'OpinionMiningTest',
            'platform': 'Twitter',
            'timestamp': str(datetime(2017, 1, 1, 1, 11, 11, 387893))
        }, {
            'text': 'This is another test',
            'sentiment': 'negative',
            'keyword': 'OpinionMiningTest',
            'platform': 'Facebook',
            'timestamp': str(datetime(2017, 2, 1, 1, 11, 11, 387893))
        }]
        formatted_data = {
            'tweets': [{
                'timestamp': '2017-01-01 01:11:11.387893',
                'platform': 'Twitter',
                'sentiment': 'positive',
                'keyword': 'OpinionMiningTest',
                'text': 'This is a test'
            }, {
                'timestamp': '2017-02-01 01:11:11.387893',
                'platform': 'Facebook',
                'sentiment': 'negative',
                'keyword': 'OpinionMiningTest',
                'text': 'This is another test'
            }],
            'sentiment': {
                'negative': 1,
                'positive': 1
            },
            'coordinates': [],
            'total': 2
        }
        self.assertEqual(format_data(data), formatted_data)
