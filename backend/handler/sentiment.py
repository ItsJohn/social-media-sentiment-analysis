from handler.classifiers.text.text_classification import classify
from handler.db import get_data_for_sentiment
from handler.db import insert_sentiment


def classify_data(data: list) -> list:
    new_data = []
    for entry in data:
        entry['sentiment'], entry['confidence'] = classify(entry['text'])
        new_data.append(entry)
    return new_data


def classify_and_store_data(data: list):
    for entry in data:
        classification, confidence = classify(entry['text'])
        insert_sentiment(
            entry['_id'],
            classification,
            confidence
        )


def find_sentiment():
    data = get_data_for_sentiment()
    classify_and_store_data(data)


def sentiment(text: str) -> tuple:
    return classify(text)
