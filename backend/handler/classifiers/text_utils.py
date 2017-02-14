import re
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from string import punctuation


def strip_repetitions_letters(text: str) -> str:
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", text)


def eliminate_punctuation(text: str) -> str:
    for c in punctuation:
        text = text.replace(c, "")
    return text


def eliminate_stop_words(text: str) -> list:
    filtered_sentence = []
    stop = set(stopwords.words('english'))
    word_tokens = TweetTokenizer().tokenize(text)

    for w in word_tokens:
        if w not in stop:
            filtered_sentence.append(w)

    return filtered_sentence


def process_text(text: str) -> list:
    # Convert to lower case
    text = text.lower()
    # Removes @username
    text = re.sub('@[^\s]+', '', text)
    # Remove additional white spaces
    text = re.sub('[\s]+', ' ', text)
    # Replace #word with word
    text = re.sub(r'#([^\s]+)', r'\1', text)
    # Eliminates the punctuation
    text = eliminate_punctuation(text)
    # Eliminates the repetitive characters
    text = strip_repetitions_letters(text)
    # Removes the stop words
    text = eliminate_stop_words(text)

    return text
