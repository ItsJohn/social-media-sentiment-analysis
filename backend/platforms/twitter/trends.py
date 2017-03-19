from pytrends.request import TrendReq

import os.path
import pickle

from platforms.twitter.twitter_api import appAuth
from handler.slack import send_report

GOOGLE_USER = {
    'NAME': 'sentimentanalysisoftwitter@gmail.com',
    'PASSWORD': 'sentiment'
}
LOCATION = {
    'UNITED_KINGDOM': '9',
    'UNITED_STATES': '1',
    'IRELAND': 23424803
}
TWITTER_API = appAuth()
TRENDS_PICKLE = 'platforms/twitter/pickle/trends.pickle'


def retrieve_trends():
    pytrend = TrendReq(
        GOOGLE_USER['NAME'],
        GOOGLE_USER['PASSWORD'],
        custom_useragent='My Pytrends Script'
    )
    trends = []

    try:
        google_trends = pytrend.hottrends({})
        trends.extend(google_trends[LOCATION['UNITED_STATES']])
        trends.extend(google_trends[LOCATION['UNITED_KINGDOM']])
    except Exception as e:
        print(e)

    try:
        twitter_trends = TWITTER_API.trends_place(
            LOCATION['IRELAND']
        )[0]['trends']
        names = [trend['name'] for trend in twitter_trends]
        trends.extend(names)
    except Exception as e:
        print(e)

    structured_trends = []
    for word in set(trends):
        trend = {}
        trend['formatted_word'] = word
        trend['search_word'] = word.replace(' ', '+')
        structured_trends.append(trend)

    return structured_trends


def check_if_trends_already_exist(old_trends):
    trends = retrieve_trends()
    new_trends = []
    for trend in trends:
        for old_trend in old_trends:
            if trend['formatted_word'] == old_trend['formatted_word']:
                trend = old_trend
                trend['use_since'] = False
        new_trends.append(trend)
    return new_trends


def load_trends_from_pickle():
    if os.path.isfile(TRENDS_PICKLE):
        with open(TRENDS_PICKLE, 'rb') as ph:
            trends = pickle.load(ph)
        return check_if_trends_already_exist(trends)
    return retrieve_trends()
