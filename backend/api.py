from flask import Flask, session
from flask.ext import restful
from requests import put, get
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

import handler.db as db
from handler.utils.twitter_api import query_twitter_for_tweets
from handler.utils.tweet_utils import extract_tweet
from handler.sentiment import classify_tweets

app = Flask(__name__)
CORS(app)
api = restful.Api(app)


class Keywords(restful.Resource):
    def get(self):
        keywords = db.get_keywords()
        return keywords


class GetTotalSentimentValue(restful.Resource):
    def get(self, term):
        stats = db.retrieve_tweets(term)
        if stats['total'] is 0:
            data = extract_tweet(
                query_twitter_for_tweets(term)['statuses'],
                term
            )
            db.insert_data(data)
            classify_tweets(data)
            stats = db.retrieve_tweets(term)
        return stats


api.add_resource(Keywords, '/api/keywords')
api.add_resource(
    GetTotalSentimentValue,
    '/api/getTotalSentiment/<string:term>'
)


if __name__ == '__main__':
    app.run(debug=True)
