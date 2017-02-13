from nltk.probability import FreqDist
from random import shuffle
from math import floor
import os.path
import pickle

from handler.classifiers.text_utils import process_text

DOCUMENTS = 'documents.txt'
WORD_FEATURE = 'word_features.txt'
ALL_WORDS = './handler/classifiers/pickle/all_words.pickle'

word_features = []
if os.path.isfile(ALL_WORDS):
    with open(ALL_WORDS, 'rb') as ph:
        old_words = pickle.load(ph)
    word_features.extend(old_words)


def open_files(sentiment, the_file):
    all_tweets = []
    all_words = []
    with open(the_file) as fh:
        for tweet in fh:
            words = process_text(tweet[:-1])
            if words:
                all_words.extend(words)
                all_tweets.append((words, sentiment))
    return all_tweets, all_words


def check_if_words_exist_in_features(tweet):
    feature = {}
    if tweet:
        words = set(tweet)
        for word in word_features:
            feature[word] = False
        for word in words:
            feature[word] = (word in word_features)
    return feature


def manipulate_data(all_tweets):
    shuffle(all_tweets)

    print('Recognizing words...')
    featuresets = []
    for (tweet, category) in all_tweets:
        features = check_if_words_exist_in_features(tweet)
        featuresets.append((features, category))
    return featuresets


def getData(file_number):
    print('Loading Tweets from file...')
    all_tweets, all_words = open_files(
        'positive',
        './handler/classifiers/sentiment_files/pos' + str(file_number) + '.txt'
    )
    tweets, words = open_files(
        'negative',
        './handler/classifiers/sentiment_files/neg' + str(file_number) + '.txt'
    )
    all_tweets.extend(tweets)
    all_words.extend(words)

    # Get the most used from all the words
    known_words = list(FreqDist(all_words).keys())
    with open('./handler/classifiers/pickle/all_words.pickle', 'wb') as ph:
        pickle.dump(known_words, ph)

    return manipulate_data(all_tweets)


def format_data(tweet):
    return check_if_words_exist_in_features(process_text(tweet))
