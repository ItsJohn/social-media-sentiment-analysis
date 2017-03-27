from handler.classifiers.classifier_utils import fit_classifiers
from handler.classifiers.classifier_utils import test_classifier_accuracy
from handler.classifiers.classifier_utils import validate_classifiers
from handler.classifiers.classifier_utils import predict_classifier
from handler.classifiers.classifier_utils import get_classifier_names
from handler.classifiers.classifier_utils import load_classifier

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from handler.classifiers.text.utils import get_stop_words
from handler.classifiers.text.utils import tokenize
from handler.utilities import save_this
from handler.utilities import open_this
import os.path

PICKLE_PATH = 'handler/classifiers/pickle/'

# Loads or creates the CountVectorizer which will
# format and track the bag of words
if os.path.isfile(PICKLE_PATH + 'count_vect.pickle'):
    count_vect = open_this(PICKLE_PATH + 'count_vect.pickle')
else:
    count_vect = CountVectorizer(
        ngram_range=(1, 3),
        stop_words=get_stop_words(),
        tokenizer=tokenize
    )

if os.path.isfile(PICKLE_PATH + 'tf_transformer.pickle'):
    tf_transformer = open_this(PICKLE_PATH + 'tf_transformer.pickle')
else:
    tf_transformer = TfidfTransformer()


def prepare_new_data(data):
    """ Vectorizes data for prediction and preforms processes text,
        and term frequency inverse """
    X_counts = count_vect.transform(data)
    X_tfidf = tf_transformer.transform(X_counts)
    return X_tfidf


def prepare_training_data(data):
    """ Trains vertorizers """
    X_train_counts = count_vect.fit_transform(data)
    X_train_tfidf = tf_transformer.fit_transform(X_train_counts)
    save_this(PICKLE_PATH + 'count_vect.pickle', count_vect)
    save_this(PICKLE_PATH + 'tf_transformer.pickle', tf_transformer)
    return X_train_tfidf


def train_classifiers(data: list, classification: list):
    """ Prepares text data and trains classifiers """
    data = prepare_training_data(data)
    fit_classifiers(data, classification)


def test_classifiers(data: list, classification: list):
    """ Prepares text data and tests classifiers """
    data = prepare_new_data(data)
    test_classifier_accuracy(data, classification)


def cross_validation(data: list, classification: list):
    """ Prepares text data and uses cross validation on classifiers """
    print('Preparing data for Cross Validation')
    data = prepare_new_data(data)
    print('Cross Validating...')
    for name in get_classifier_names():
        classifier = load_classifier(name)
        validate_classifiers(data, classification, classifier, name)


def classify(data: str) -> tuple:
    """ Prepares text data and classifies text """
    data = prepare_new_data([data])
    return predict_classifier(data)
