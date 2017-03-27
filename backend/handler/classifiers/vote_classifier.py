from nltk.classify import ClassifierI
from statistics import mode


class VoteClassifier(ClassifierI):

    def __init__(self, *classifiers):
        self._classifiers = classifiers[0]

    def get_classifications(self, features):
        """
            Each classifier mentioned in classifier_utils.py
            in the classifier variable predicts the classification
            of the features
        """
        votes = []
        for classifier in self._classifiers:
            v = classifier.predict(features)
            votes.extend(v)

        return votes

    def predict(self, features):
        """ Predicts the classification and returns the majority vote """
        return mode(self.get_classifications(features))

    def predict_and_confidence(self, features):
        """ Predicts the classification and creates a confidence level """
        classification = self.get_classifications(features)
        choice_votes = classification.count(mode(classification))
        conf = choice_votes / len(classification)
        return mode(classification), conf
