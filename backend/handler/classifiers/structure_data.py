from nltk.probability import FreqDist
from random import shuffle
from math import floor
import os.path
import pickle

from handler.classifiers.text_utils import process_text

DOCUMENTS = 'documents.txt'
WORD_FEATURE = 'word_features.txt'
PICKLE_PATH = './handler/classifiers/pickle/'

word_features = []
if os.path.isfile(PICKLE_PATH + 'all_words.pickle'):
    with open(PICKLE_PATH + 'all_words.pickle', 'rb') as ph:
        old_words = pickle.load(ph)
    word_features.extend(old_words)


def open_files(sentiment, the_file):
    all_data = []
    all_words = []
    with open(the_file) as fh:
        for data in fh:
            words = process_text(data[:-1])
            if words:
                all_words.extend(words)
                all_data.append((words, sentiment))
    return all_data, all_words


def check_if_words_exist_in_features(data):
    feature = {}
    if data:
        new_features = word_features[:floor(len(word_features) / 2)]
        for word in new_features:
            feature[word] = False
        for word in set(data):
            feature[word] = (word in new_features)
    return feature


def manipulate_data(all_data):
    shuffle(all_data)

    print('Recognizing words...')
    featuresets = []
    for (data, category) in all_data:
        features = check_if_words_exist_in_features(data)
        featuresets.append((features, category))
    return featuresets


def getData(**kwargs):
    all_data = []
    print('Loading data from file...')
    for sentiment, file_name in kwargs.items():
        data, all_words = open_files(sentiment, file_name)
        all_data.extend(data)
        word_features.extend(all_words)

    # Get the most used from all the words
    known_words = list(FreqDist(word_features).keys())
    with open(PICKLE_PATH + 'all_words.pickle', 'wb') as ph:
        pickle.dump(known_words, ph)

    return manipulate_data(all_data)


def format_data(data):
    return check_if_words_exist_in_features(process_text(data))
