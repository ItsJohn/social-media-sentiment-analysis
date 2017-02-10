from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import LinearSVC

from nltk.classify.scikitlearn import SklearnClassifier

import os.path
import pickle

LOCATION = 'handler/classifiers/pickle/'

classifiers_names = ['MNB', 'BNB', 'LR', 'SGDC', 'LSVC']
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
    if os.path.isfile(LOCATION + name + '_classifier.pickle'):
        with open(LOCATION + name + '_classifier.pickle', 'rb') as ph:
            classifier = pickle.load(ph)
    else:
        classifier = SklearnClassifier(classifiers[name])
    return classifier
