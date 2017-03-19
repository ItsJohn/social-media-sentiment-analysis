from handler.data_utils import format_data

from datetime import datetime
import unittest


class Data_utils_test(unittest.TestCase):

    def test_format_data(self):
        data = [{
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
        formatted_data = {
            'sentiment': {
                'positive': 1,
                'negative': 1
            },
            'newest': '2017-02-01 01:11:11',
            'graph': {
                'positive': [{
                    'x': '2017-01-01 01:11:11',
                    'y': 1
                }],
                'negative': [{
                    'x': '2017-02-01 01:11:11',
                    'y': 1
                }]
            },
            'tweets': [{
                'sentiment': 'positive',
                'keyword': 'OpinionMiningTest',
                'platform': 'Twitter',
                'timestamp': '2017-01-01 01:11:11',
                'text': 'This is a test'
            }, {
                'sentiment': 'negative',
                'keyword': 'OpinionMiningTest',
                'platform': 'Facebook',
                'timestamp': '2017-02-01 01:11:11',
                'text': 'This is another test'
            }],
            'latest': '2017-01-01 01:11:11',
            'total': 2,
            'coordinates': []
        }
        self.assertEqual(format_data(data), formatted_data)
