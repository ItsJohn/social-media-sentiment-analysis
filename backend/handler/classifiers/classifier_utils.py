from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import LinearSVC

from nltk.classify.scikitlearn import SklearnClassifier

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
