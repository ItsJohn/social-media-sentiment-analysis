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


FILE_NUMBER = 5
POSFILE = 'handler/classifiers/sentiment_files/pos' + str(file_number) + '.txt'
NEGFILE = 'handler/classifiers/sentiment_files/neg' + str(file_number) + '.txt'
PICKLE_PATH = './handler/classifiers/pickle/'


def test_classifier(name, classifier, data):
    percentage = ((accuracy(classifier, data) * 100))
    print(name, "accuracy percent:", percentage)
    if name is "Final":
        send_completed_message(percentage)


data = getData(POSFILE, NEGFILE)

divide = int(floor(len(data) / 2))
training_set = np.array(data[:divide])
testing_set = np.array(data[divide:])

print('Prepare training data...')
new_models = []
kfold = model_selection.KFold(n_splits=10, shuffle=True, random_state=7)
for name in get_classifier_names():
    classifier = load_classifier(name)
    print('Training and testing', name, '...')
    for traincv, testcv in kfold.split(training_set):
        classifier.train(training_set[traincv])
        test_classifier(name, classifier, training_set[testcv])
    with open(
        PICKLE_PATH + name + '_classifier.pickle',
        'wb'
    ) as ph:
        pickle.dump(classifier, ph)
    new_models.append(classifier)

print('Voting on classifier prediction...')
voted_classifier = VoteClassifier(new_models)
test_classifier("Final", voted_classifier, testing_set)
