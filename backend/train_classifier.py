import pickle
import numpy as np

from sklearn import model_selection
from nltk.classify.util import accuracy
from math import floor

from handler.slack import send_completed_message
from handler.classifiers.structure_data import getData
from handler.classifiers.vote_classifier import VoteClassifier
from handler.classifiers.classifier_utils import get_classifier_names
from handler.classifiers.classifier_utils import load_classifier


FILE_NUMBER = 1
DIR = 'handler/classifiers/'
NEW_SENTIMENT_FOLDER = DIR + 'sentiment_files/'


POSFILE = NEW_SENTIMENT_FOLDER + 'pos' + str(FILE_NUMBER) + '.txt'
NEGFILE = NEW_SENTIMENT_FOLDER + 'neg' + str(FILE_NUMBER) + '.txt'

PICKLE_PATH = DIR + 'pickle/'

data = getData(positive=POSFILE, negative=NEGFILE)


def test_classifier(name, classifier, data):
    percentage = ((accuracy(classifier, data) * 100))
    print(name, "accuracy percent:", percentage)
    if name is "Final":
        send_completed_message(percentage)


def train_classifiers(data):
    for name in get_classifier_names():
        classifier = load_classifier(name)
        print('Training', name, '...')
        classifier.train(data)
        with open(
            PICKLE_PATH + name + '_classifier.pickle',
            'wb'
        ) as ph:
            pickle.dump(classifier, ph)


def validate_classifiers(data):
    kfold = model_selection.KFold(n_splits=10, shuffle=True, random_state=7)
    for name in get_classifier_names():
        classifier = load_classifier(name)
        print('Training and testing', name, '...')
        for traincv, testcv in kfold.split(data):
            classifier.train(data[traincv])
            test_classifier(name, classifier, data[testcv])
        with open(
            PICKLE_PATH + name + '_classifier.pickle',
            'wb'
        ) as ph:
            pickle.dump(classifier, ph)


print('Prepare training data...')
cv_test_split = int(floor(len(data) * 0.5))
cross_validation_set = np.array(data[:cv_test_split])
testing_set = np.array(data[cv_test_split:])

new_models = []
for name in get_classifier_names():
    classifier = load_classifier(name)
    new_models.append(classifier)

print('Voting on classifier prediction...')
voted_classifier = VoteClassifier(new_models)
test_classifier("Final", voted_classifier, testing_set)
