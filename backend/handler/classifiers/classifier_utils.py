from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import LinearSVC
from handler.classifiers.vote_classifier import VoteClassifier

from sklearn import model_selection
from sklearn.metrics import accuracy_score

from nltk.classify.scikitlearn import SklearnClassifier
from nltk.classify.util import accuracy

from handler.slack import send_completed_message
from random import shuffle
from typing import Union
import numpy as np

import os.path
import pickle

PICKLE_PATH = 'handler/classifiers/pickle/'

classifiers_names = [
    'Multinomial_Naive_Bayes',
    'Bernoulli_Naive_Bayes',
    'Logistic_Regression',
    'Stochastic_Gradient_Descent',
    'Linear_SVM'
]
classifiers = {
    classifiers_names[0]: MultinomialNB(),
    classifiers_names[1]: BernoulliNB(),
    classifiers_names[2]: LogisticRegression(),
    classifiers_names[3]: SGDClassifier(),
    classifiers_names[4]: LinearSVC()
}


def get_classifier_names():
    return classifiers_names


def load_classifier(name):
    if os.path.isfile(PICKLE_PATH + name + '_classifier.pickle'):
        with open(PICKLE_PATH + name + '_classifier.pickle', 'rb') as ph:
            classifier = pickle.load(ph)
    else:
        classifier = SklearnClassifier(classifiers[name])
    return classifier


def test_classifier(
    name: str,
    classifier: VoteClassifier,
    data: Union[np.array, list]
):
    percentage = (accuracy(classifier, data) * 100)
    print(name, "accuracy percent:", percentage)
    if name is "Final":
        send_completed_message(percentage)


def train_classifiers(data: Union[np.array, list]):
    for name in get_classifier_names():
        classifier = load_classifier(name)
        print('Training', name, '...')
        classifier.train(data)
        with open(
            PICKLE_PATH + name + '_classifier.pickle',
            'wb'
        ) as ph:
            pickle.dump(classifier, ph)


def validate_classifiers(data: Union[np.array, list]):
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


def voted_classifier(data: Union[np.array, list]):
    new_models = []
    for name in get_classifier_names():
        classifier = load_classifier(name)
        new_models.append(classifier)

    print('Voting on classifier prediction...')
    classifier = VoteClassifier(new_models)
    test_classifier("Final", classifier, data)
