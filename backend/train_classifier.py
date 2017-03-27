from sklearn.model_selection import train_test_split

from handler.classifiers.text.structure_data import getData

from handler.classifiers.classifier_utils import get_classifier_names
from handler.classifiers.classifier_utils import load_classifier

from handler.classifiers.text.text_classification import train_classifiers
from handler.classifiers.text.text_classification import cross_validation

# Point to training datasets
NEW_CATEGORY_FOLDER = 'sentiment_files'
FILE_NUMBER = 1

DIR = 'handler/classifiers/text/' + NEW_CATEGORY_FOLDER + '/'

POSFILE = DIR + 'positive' + str(FILE_NUMBER) + '.txt'
NEGFILE = DIR + 'negative' + str(FILE_NUMBER) + '.txt'

# generates data in the right format for classifiers
data = getData(positive=POSFILE, negative=NEGFILE)

print('Prepare training data...')
validation_size = 0.8
seed = 42

# Seperates data into training and test datasets 80/20 split
X_train, X_test, Y_train, Y_test = train_test_split(
    data['data'],
    data['category'],
    test_size=validation_size,
    random_state=seed
)

# trains and tests classifiers
train_classifiers(X_train, Y_train)
cross_validation(X_test, Y_test)
