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


def eliminate_stop_words(word_tokens: list) -> list:
    filtered_sentence = []
    exceptions = set((
        'couldn',
        'didn',
        'doesn',
        'hadn',
        'hasn',
        'haven',
        'mightn',
        'mustn',
        'shouldn',
        'wasn',
        'weren',
        'wouldn',
        'not'
    ))
    stop = set(stopwords.words('english')) - exceptions

    for w in word_tokens:
        if w not in stop:
            filtered_sentence.append(w)

    return filtered_sentence


def remove_username(text: str) -> str:
    """
        Removes Twitter usernames
        e.g @user
    """
    return re.sub('@[^\s]+', '', text)


def removes_additional_whitespace(text: str) -> str:
    return re.sub('[\s]+', ' ', text)


def replaces_hashtags_with_word(text: str) -> str:
    """
        Replaces hashtags with the word
        e.g #word -> word
    """
    return re.sub(r'#([^\s]+)', r'\1', text)


def tokenize(text: str) -> list:
    """
        Splits the sentence into tokens
        e.g ['Splits', 'the', 'sentence', 'into', 'tokens']
    """
    return TweetTokenizer().tokenize(text)


def process_text(text: str) -> list:
    # Convert to lower case
    text = text.lower()
    text = remove_username(text)
    text = removes_additional_whitespace(text)
    text = replaces_hashtags_with_word(text)
    text = eliminate_punctuation(text)
    text = strip_repetitions_letters(text)
    tokenized_text = tokenize(text)
    tokenized_text = eliminate_stop_words(tokenized_text)

    return tokenized_text
