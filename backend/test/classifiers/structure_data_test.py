import handler.classifiers.text.structure_data as sd

import unittest
from test.utils import sort_tuple_list
from os import remove
from os import path


class Structure_data_test(unittest.TestCase):

    def setUp(self):
        sd.PICKLE_PATH = 'test/mock/'
        sd.word_features = ['different', 'word', 'sentence']

    def test_open_files(self):
        format_data = (['this is a sentence in a file'], ['positive'])
        self.assertTrue(path.exists(sd.PICKLE_PATH + 'test.txt'))
        self.assertEqual(
            sd.open_files('positive', sd.PICKLE_PATH + 'test.txt'),
            format_data
        )
