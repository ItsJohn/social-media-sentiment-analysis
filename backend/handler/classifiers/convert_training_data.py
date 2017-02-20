import csv
import os


# FILE_NAME: The name of the file you want to convert
# SENTIMENT_COLUMN: The column number that contains the sentiment
# TEXT_COLUMN: The column number that contains the text
# DIR: The name of the directory you want to save the coverted files
# SENTENCES_PER_FILE: The number of entries in a file
# HAS_TABLE_HEADER: Whether the file contains a column that names columns
# SENTIMENT: A dictionary that contains the how the sentiment is expressed in
#       the file is mapped to the name for the converted file


FILE_NAME = 'Twitter-sentiment-self-drive-DFE.csv'
SENTIMENT_COLUMN = 5
TEXT_COLUMN = 10
DIR = 'five_category_sentiment/'
SENTENCES_PER_FILE = 5000
HAS_TABLE_HEADER = False
SENTIMENT = {
    '5': 'very_positive',
    '4': 'positive',
    '3': 'nuetral',
    '2': 'negative',
    '1': 'very_negative',
    'not_relevant': 'not_relevant'
}


all_data = {}


def open_file():
    with open(FILE_NAME, 'r', encoding='latin-1') as fh:
        reader = csv.reader(fh)
        for line in reader:
            yield line


def store_data(sentiment):
    sentiment['count'] = sentiment['count'] + 1
    with open(
        DIR + sentiment['label'] + str(sentiment['count']) + '.txt',
        'w'
    ) as fh:
        for text in sentiment['text']:
            print(text, file=fh)
    sentiment['text'] = []
    return sentiment


def seperateWords(data):
    global all_data

    if data[SENTIMENT_COLUMN] in all_data:
        sentiment = all_data[data[SENTIMENT_COLUMN]]
        sentiment['text'].append(data[TEXT_COLUMN])
        if len(sentiment['text']) == SENTENCES_PER_FILE:
            all_data[data[SENTIMENT_COLUMN]] = store_data(
                sentiment
            )
    else:
        all_data[data[SENTIMENT_COLUMN]] = {
            'text': [data[TEXT_COLUMN]],
            'count': 0,
            'label': SENTIMENT[data[SENTIMENT_COLUMN]]
        }


if not os.path.exists(DIR):
    os.makedirs(DIR)


row_number = 0
for sentence in open_file():
    if not HAS_TABLE_HEADER and row_number is not 0:
        seperateWords(sentence)
    else:
        row_number = row_number + 1

for element in all_data:
    store_data(
        all_data[element]
    )