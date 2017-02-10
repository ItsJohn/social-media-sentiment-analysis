import csv

tweets_per_file = 5000


def getTweets():
    with open('dataset.csv', 'r') as fh:
        reader = csv.reader(fh)
        for line in reader:
            yield line


def seperateWords(tweet, posC, negC, negitive_text, positive_text):
    sentiment = 1
    text = 3
    positive = '1'
    if tweet[sentiment] == positive:
        positive_text.append(tweet[text])
        if len(positive_text) == tweets_per_file:
            posC = posC + 1
            with open('sentiment_files/pos' + str(posC) + '.txt', 'w') as fh:
                for text in positive_text:
                    print(text, file=fh)
            positive_text = []
    else:
        negitive_text.append(tweet[text])
        if len(negitive_text) == tweets_per_file:
            negC = negC + 1
            with open('sentiment_files/neg' + str(negC) + '.txt', 'w') as fh:
                for text in negitive_text:
                    print(text, file=fh)
            negitive_text = []
    return posC, negC, negitive_text, positive_text


def createFiles():
    posC = 0
    negC = 0
    negitive_text = []
    positive_text = []
    counter = 0
    for i in getTweets():
        if counter is not 0:
            posC, negC, negitive_text, positive_text = seperateWords(i, posC, negC, negitive_text, positive_text)
        else:
            counter = counter + 1




createFiles()
