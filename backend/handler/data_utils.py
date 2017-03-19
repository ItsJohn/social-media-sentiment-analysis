from datetime import datetime
import pandas as pd
import numpy as np
import math


def format_date(date: str) -> datetime:
    return datetime.strptime(date, '%Y-%m-%d %H:%M:%S')


def prepare_timestamp(timestamp: list):
    score = [1 for i in range(len(timestamp))]

    sentiment_df = pd.DataFrame()
    sentiment_df['timestamp'] = timestamp
    sentiment_df['sentiment'] = score
    sentiment_df.index = sentiment_df['timestamp']
    sentiment_df['timestamp'] = pd.to_datetime(sentiment_df['timestamp'])

    return sentiment_df


def graph_data(data: list, sentiments: dict):
    count = {}
    total = 0

    term_data = []
    graph_sentiment = {}
    for sentiment in sentiments.keys():
        count[sentiment] = len(sentiments[sentiment])
        total = total + len(sentiments[sentiment])
        actual_data = prepare_timestamp(sentiments[sentiment])

        # By minute
        graph_data = actual_data.resample('T').sum()
        if len(graph_data) > 200:
            # By Hour
            graph_data = actual_data.resample('H').sum()
        elif len(graph_data) < 10:
            # By Second
            graph_data = actual_data.resample('S').sum()

        y_axis = graph_data.values.tolist()
        x_axis = graph_data.index.to_pydatetime().tolist()

        graph_sentiment[sentiment] = []
        for i, value in enumerate(x_axis):
            graph_sentiment[sentiment].append({
                'x': str(value),
                'y': int(0 if math.isnan(y_axis[i][0]) else y_axis[i][0])
            })

    return graph_sentiment, count, total


def format_data(data: list) -> dict:
    """ Translates data into JSON  """
    coordinates = []
    sentiments = {}
    timelines = []
    for content in data:
        if content['sentiment'] not in sentiments:
            sentiments[content['sentiment']] = []
        timestamp = format_date(content['timestamp'])
        sentiments[content['sentiment']].append(timestamp)
        if 'coordinates' in content:
            coordinates.append({
                'lng': content['coordinates'][0],
                'lat': content['coordinates'][1]
            })
        timelines.append(timestamp)
    line_graph, count, total = graph_data(data, sentiments)

    return {
        'total': total,
        'sentiment': count,
        'coordinates': coordinates,
        'graph': line_graph,
        'newest': str(max(timelines)),
        'latest': str(min(timelines)),
        'tweets': data
    }
