from handler.classifiers.vote_classifier import VoteClassifier

from sklearn import model_selection

from sklearn.metrics import accuracy_score

from handler.utilities import save_this
from handler.utilities import open_this
import os.path


# TODO: import necessary algorithms
from handler.classifiers.text.text_classifiers import classifiers
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import LinearSVC


PICKLE_PATH = 'handler/classifiers/pickle/'


def get_classifier_names():
    return list(classifiers.keys())


def load_classifier(name):
    if os.path.isfile(PICKLE_PATH + name + '_classifier.pickle'):
        classifier = open_this(PICKLE_PATH + name + '_classifier.pickle')
    else:
        classifier = classifiers[name]
    return classifier


def build_model():
    """ Creates a new model using all of the classifiers mentioned above """
    new_models = []
    for name in get_classifier_names():
        classifier = load_classifier(name)
        new_models.append(classifier)
    classifier = VoteClassifier(new_models)
    return classifier


def fit_classifiers(data: list, classification: list):
    """ Trains the above classifiers  """
    for name in get_classifier_names():
        classifier = load_classifier(name)
        print('Training', name, '...')
        classifier.fit(data, classification)
        save_this(PICKLE_PATH + name + '_classifier.pickle', classifier)


def validate_classifiers(data: list, classification: list, classifer, name):
    """ Uses cross validation to test how the classifiers act on unseen data"""
    scores = model_selection.cross_val_score(
        classifer,
        data,
        classification,
        cv=5
    )
    print(name, "Accuracy: %0.2f (+/- %0.2f)" % (
        scores.mean() * 100,
        scores.std() * 2
    ))


def test_classifier_accuracy(data: list, classification: list):
    """ Tests the accuracy of the new classifier
        from the build_model() function """
    print('Voting on classifier prediction...')
    classifier = build_model()

    prediction = []
    for i, value in enumerate(data):
        prediction.append(classifier.predict(value))

    percentage = accuracy_score(prediction, classification) * 100
    print("Accuracy percent:", percentage)


def predict_classifier(data) -> tuple:
    """ Predicts the classification of new data """
    classifier = build_model()
    return classifier.predict_and_confidence(data)
