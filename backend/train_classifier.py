import numpy as np

from sklearn.model_selection import train_test_split

from handler.classifiers.structure_data import getData

from handler.classifiers.classifier_utils import get_classifier_names
from handler.classifiers.classifier_utils import load_classifier

from handler.classifiers.classifier_utils import validate_classifiers
from handler.classifiers.classifier_utils import test_classifier
from handler.classifiers.classifier_utils import voted_classifier

DIR = 'handler/classifiers/'

NEW_SENTIMENT_FOLDER = DIR + 'sentiment_files' + '/'

FILE_NUMBER = 1

POSFILE = NEW_SENTIMENT_FOLDER + 'neg' + str(FILE_NUMBER) + '.txt'
NEGFILE = NEW_SENTIMENT_FOLDER + 'pos' + str(FILE_NUMBER) + '.txt'


data = getData(positive=POSFILE, negative=NEGFILE)


print('Prepare training data...')
validation_size = 0.5
seed = 7
train, test = train_test_split(
    data,
    test_size=validation_size,
    random_state=seed
)

validate_classifiers(np.array(train))
voted_classifier(np.array(test))
