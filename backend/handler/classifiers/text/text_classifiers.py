from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import LinearSVC

classifiers = {
    'Multinomial_Naive_Bayes': MultinomialNB(),
    'Logistic_Regression': LogisticRegression(),
    'LinearSVC': LinearSVC()
}
