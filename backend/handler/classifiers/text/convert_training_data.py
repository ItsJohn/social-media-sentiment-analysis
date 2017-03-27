import csv
import os


# FILE_NAME: The name of the file you want to convert
# CATEGORY_COLUMN: The column number that contains the categories
#       Columns Number Start at 0
# TEXT_COLUMN: The column number that contains the text
# DIR: The name of the directory you want to save the coverted files
# SENTENCES_PER_FILE: The number of entries in a file
# HAS_TABLE_HEADER: Whether the file contains a column that names columns
# CATEGORIES: A dictionary that contains the how the category is expressed in
#       the file is mapped to the name for the converted file


FILE_NAME = 'smsSpam.csv'
CATEGORY_COLUMN = 0
TEXT_COLUMN = 1
DIR = 'spam' + '/'
SENTENCES_PER_FILE = 10000000
HAS_TABLE_HEADER = True
CATEGORIES = {
    'spam': 'spam',
    'ham': 'notspam'
}


all_data = {}


def open_file():
    with open(FILE_NAME, 'r', encoding='latin-1') as fh:
        reader = csv.reader(fh)
        for line in reader:
            yield line


def store_data(category: dict) -> dict:
    category['count'] = category['count'] + 1
    with open(
        DIR + category['label'] + str(category['count']) + '.txt',
        'w'
    ) as fh:
        for text in category['text']:
            print(text, file=fh)
    category['text'] = []
    return category


def seperateWords(data: list):
    global all_data

    if data[CATEGORY_COLUMN] in CATEGORIES:
        if data[CATEGORY_COLUMN] in all_data:
            category = all_data[data[CATEGORY_COLUMN]]
            category['text'].append(data[TEXT_COLUMN])
            if len(category['text']) == SENTENCES_PER_FILE:
                all_data[data[CATEGORY_COLUMN]] = store_data(
                    category
                )
        else:
            all_data[data[CATEGORY_COLUMN]] = {
                'text': [data[TEXT_COLUMN]],
                'count': 0,
                'label': CATEGORIES[data[CATEGORY_COLUMN]]
            }


if not os.path.exists(DIR):
    os.makedirs(DIR)


row_number = 0
for sentence in open_file():
    if not HAS_TABLE_HEADER or row_number is not 0:
        seperateWords(sentence)
    else:
        row_number = row_number + 1

for element in all_data:
    store_data(
        all_data[element]
    )
