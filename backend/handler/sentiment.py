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


def classify_tweets(data: list):
    new_tweets = []
    for tweet in data:
        feats = format_data(tweet['text'])
        tweet['sentiment'], tweet[
            'confidence'] = voted_classifier.confidence(feats)
        new_tweets.append(tweet)
    return new_tweets


def classify_and_store_tweets(data: list):
    for tweet in data:
        feats = format_data(tweet['text'])
        classification, confidence = voted_classifier.confidence(feats)
        insert_sentiment(
            tweet['_id'],
            classification,
            confidence
        )


def find_sentiment():
    data = get_data_for_sentiment()
    classify_and_store_tweets(data)


def sentiment(text: str):
    feats = format_data(text)
    return voted_classifier.confidence(feats)
