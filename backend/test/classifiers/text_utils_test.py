from handler.classifiers.text_utils import strip_repetitions_letters
from handler.classifiers.text_utils import eliminate_punctuation
from handler.classifiers.text_utils import eliminate_stop_words
from handler.classifiers.text_utils import process_text

from test.utils import format_data
import unittest


class Text_Utils_test(unittest.TestCase):

    def test_strip_repetitions_letters(self):
        data = 'This sentence is sooooooo loooooooooong'
        format_data = 'This sentence is soo loong'
        self.assertEqual(strip_repetitions_letters(data), format_data)
        self.assertEqual(strip_repetitions_letters(""), "")

    def test_eliminate_punctuation(self):
        data = "This sentence doesn't mean anything, (or does it)?"
        format_data = 'This sentence doesnt mean anything or does it'
        self.assertEqual(eliminate_punctuation(data), format_data)
        self.assertEqual(eliminate_punctuation(""), "")

    def test_eliminate_stop_words(self):
        data = ['This', 'sentence', 'is', 'not', 'important']
        format_data = ['This', 'sentence', 'not', 'important']
        self.assertEqual(eliminate_stop_words(data), format_data)
        self.assertEqual(eliminate_stop_words(""), [])

    def test_process_text(self):
        data = "@sentence THIS IS A TEST! #Code #seeeeeennnnnttteeennnnncce"
        format_data = ['test', 'code', 'seenntteenncce']
        self.assertEqual(process_text(data), format_data)
        self.assertEqual(process_text(''), [])
