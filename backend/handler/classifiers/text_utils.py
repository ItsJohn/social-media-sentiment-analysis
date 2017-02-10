import re
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from string import punctuation


def strip_repetitions_letters(text):
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", text)


def eliminate_punctuation(text):
    for c in punctuation:
        text = text.replace(c, "")
    return text


def eliminate_stop_words(text):
    filtered_sentence = []
    stop = set(stopwords.words('english'))
    word_tokens = TweetTokenizer().tokenize(text)

    for w in word_tokens:
        if w not in stop:
            filtered_sentence.append(w)

    return filtered_sentence


# not used yet
def remove_punctuation(words):
    new_words = []
    for word in words:
        front = False
        back = False
        if word in punctuation:
            word = ""
        else:
            while ((front is False) or (back is False)) and word is not "":
                if front is False:
                    if word[:1] in punctuation:
                        word = word.replace(word[:1], "")
                    else:
                        front = True
                if back is False:
                    if word[-1:] in punctuation:
                        word = word.replace(word[-1:], "")
                    else:
                        back = True
        if word is not "":
            new_words.append(word)
    return new_words


def process_text(text):
    # Convert to lower case
    text = text.lower()
    # Removes @username
    re.sub('@[^\s]+', '', text)
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
    if text:
        return text
    return False
