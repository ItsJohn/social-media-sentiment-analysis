from handler.classifiers.text.utils import strip_repetitions_letters
from handler.classifiers.text.utils import eliminate_punctuation
from handler.classifiers.text.utils import tokenize
from handler.classifiers.text.utils import get_stop_words
from handler.classifiers.text.utils import remove_username
from handler.classifiers.text.utils import removes_additional_whitespace
from handler.classifiers.text.utils import replaces_hashtags_with_word
from handler.classifiers.text.utils import process_text

from nltk.corpus import stopwords
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

    def test_tokenize(self):
        data = '@user This is a sentence #sentence :)'
        format_data = ['this', 'is', 'a', 'sentence', 'sentence']
        self.assertEqual(tokenize(data), format_data)

    def test_get_stop_words(self):
        self.assertLess(len(get_stop_words()), len(stopwords.words('english')))

    def test_remove_username(self):
        data = '@user look at this!!!'
        format_data = ' look at this!!!'
        self.assertEqual(remove_username(data), format_data)

    def test_removes_additional_whitespace(self):
        data = '@user          look at           this!!!'
        format_data = '@user look at this!!!'
        self.assertEqual(removes_additional_whitespace(data), format_data)

    def test_replaces_hashtags_with_word(self):
        data = '@user look at this!!! #something #cool'
        format_data = '@user look at this!!! something cool'
        self.assertEqual(replaces_hashtags_with_word(data), format_data)

    def test_process_text(self):
        data = "@sentence THIS IS A TEST! #Code #seeeeeennnnnttteeennnnncce"
        format_data = ' this is a test code seenntteenncce'
        self.assertEqual(process_text(data), format_data)
        self.assertEqual(process_text(''), '')
