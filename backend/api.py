from flask import Flask, session
from flask.ext import restful
from requests import put, get
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

from handler.utils.twitter_api import query_twitter_for_tweets
from handler.utils.tweet_utils import extract_tweet
from handler.classifiers.sentiment import classify_data
from handler.utils.twitter_api import search_auth
import handler.db as db

app = Flask(__name__)
CORS(app)
api = Api(app)


class Keywords(Resource):

    def get(self):
        keywords = db.get_keywords()
        return keywords


class GetTotalSentimentValue(Resource):

    def get(self, term):
        stats = db.retrieve_tweets(term)
        if stats['total'] is 0:
            data = extract_tweet(
                query_twitter_for_tweets(term, auth=search_auth())['statuses'],
                term
            )
            stats = classify_data(data)
            db.insert_data(stats)
            stats = db.format_data(stats)
        return stats


api.add_resource(Keywords, '/api/keywords')
api.add_resource(
    GetTotalSentimentValue,
    '/api/getTotalSentiment/<string:term>'
)


if __name__ == '__main__':
    app.run(debug=True)
