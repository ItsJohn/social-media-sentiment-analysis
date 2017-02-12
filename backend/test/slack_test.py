from handler.slack import format_report

from test.utils import format_data
import unittest


class Slack_test(unittest.TestCase):

    def test_format_data(self):
        data = {
            'test': 1,
            'test2': 51
        }
        formatted_data = [{
            'color': 'good',
            'text': 'test2: 51'
        }, {
            'color': 'danger',
            'text': 'test: 1'
        }]
        self.assertEqual(format_data(format_report(data)), formatted_data)
