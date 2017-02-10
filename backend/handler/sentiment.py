import pickle

from handler.classifiers.text_utils import process_text
from handler.classifiers.structure_data import format_data
from handler.classifiers.vote_classifier import VoteClassifier
from handler.classifiers.classifier_utils import get_classifier_names
from handler.classifiers.classifier_utils import load_classifier
from handler.db import get_data_for_sentiment, insert_sentiment


def load_all_classifier():
    classifiers = []
    for name in get_classifier_names():
        classifiers.append(load_classifier(name))
    return classifiers


voted_classifier = VoteClassifier(load_all_classifier())


def classify_tweets(data):
    for tweet in data:
        feats = format_data(tweet['text'])
        insert_sentiment(
            tweet['_id'],
            voted_classifier.classify(feats),
            voted_classifier.confidence(feats)
        )


def find_sentiment():
    data = get_data_for_sentiment()
    classify_tweets(data)


def sentiment(text):
    feats = format_data(text)
    return voted_classifier.classify(feats), voted_classifier.confidence(feats)
