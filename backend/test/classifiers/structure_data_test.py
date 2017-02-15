import handler.classifiers.structure_data as sd

import unittest
from test.utils import sort_tuple_list
from os import remove
from os import path


class Structure_data_test(unittest.TestCase):

    def setUp(self):
        sd.PICKLE_PATH = 'test/mock/'
        sd.word_features = ['different', 'word', 'sentence']

    def test_manipulate_data(self):
        data = [(['This', 'sentence', 'important'], 'nuetral')]
        format_data = [({
            'This': False,
            'sentence': False,
            'different': False,
            'important': False
        }, 'nuetral')]
        self.assertEqual(sd.manipulate_data(data), format_data)

    def test_check_if_words_exist_in_features(self):
        data = ['This', 'sentence', 'important']
        format_data = {
            'This': False,
            'sentence': False,
            'different': False,
            'important': False
        }
        self.assertEqual(
            sd.check_if_words_exist_in_features(data),
            format_data
        )

    def test_open_files(self):
        format_data = (
            [(
                ['sentence', 'file'],
                'positive'
            )],
            ['sentence', 'file']
        )
        self.assertTrue(path.exists(sd.PICKLE_PATH + 'test.txt'))
        self.assertEqual(
            sd.open_files('positive', sd.PICKLE_PATH + 'test.txt'),
            format_data
        )

    def test_process_text(self):
        data = sd.PICKLE_PATH + 'test.txt'
        format_data = [({
            'sentence': False,
            'file': False,
            'word': False,
            'different': False
        }, 'positive')]
        self.assertEqual(sd.getData(positive=data), format_data)
        format_data = [({
            'different': False,
            'file': False,
            'word': False,
            'sentence': True
        }, 'negative'), ({
            'different': False,
            'file': False,
            'word': False,
            'sentence': True
        }, 'positive')]
        self.assertEqual(
            sort_tuple_list(
                sd.getData(positive=data, negative=data)
            ), format_data
        )
        remove(sd.PICKLE_PATH + "all_words.pickle")

    def test_format_data(self):
        data = "This sentence is important"
        format_data = {
            'important': False,
            'different': False,
            'sentence': False
        }
        self.assertEqual(sd.format_data(data), format_data)
