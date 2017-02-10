from nltk.classify import ClassifierI
from statistics import mode


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers[0]

    def classify(self, features):
        votes = []
        for classifier in self._classifiers:
            v = classifier.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for classifier in self._classifiers:
            v = classifier.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf
