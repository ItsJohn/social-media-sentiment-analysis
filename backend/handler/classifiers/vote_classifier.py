from nltk.classify import ClassifierI
from statistics import mode


class VoteClassifier(ClassifierI):

    def __init__(self, *classifiers):
        self._classifiers = classifiers[0]

    def get_classifications(self, features):
        votes = []
        for classifier in self._classifiers:
            v = classifier.classify(features)
            votes.append(v)
        return votes

    def classify(self, features):
        return mode(self.get_classifications(features))

    def confidence(self, features):
        classification = self.get_classifications(features)
        choice_votes = classification.count(mode(classification))
        conf = choice_votes / len(classification)
        return mode(classification), conf
