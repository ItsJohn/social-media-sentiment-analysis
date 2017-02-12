from handler.db import format_time
from handler.db import format_data

from datetime import datetime
import unittest


class DB_test(unittest.TestCase):
    data = [{
        '_id': '1',
        'text': 'This is a test',
        'sentiment': 'positive',
        'timestamp': datetime(2017, 1, 1, 1, 11, 11, 387893)
    }, {
        '_id': '2',
        'text': 'This is another test',
        'sentiment': 'negative',
        'timestamp': datetime(2017, 2, 1, 1, 11, 11, 387893)
    }]

    def test_format_date(self):
        formatted_date = [{
            'sentiment': 'positive',
            'text': 'This is a test',
            'timestamp': '2017-01-01 01:11:11.387893'
        }, {
            'sentiment': 'negative',
            'text': 'This is another test',
            'timestamp': '2017-02-01 01:11:11.387893'
        }]
        self.assertEqual(format_time(self.data), formatted_date)

    def test_format_data(self):
        formatted_data = {
            'total': 2,
            'tweets': [{
                'sentiment': 'positive',
                'text': 'This is a test',
                'timestamp': '2017-01-01 01:11:11.387893'
            }, {
                'sentiment': 'negative',
                'text': 'This is another test',
                'timestamp': '2017-02-01 01:11:11.387893'
            }],
            'sentiment': {
                'negative': 1,
                'positive': 1
            }
        }
        self.assertEqual(format_data(self.data), formatted_data)
