from flask import Flask, session
from requests import put, get
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin

from download import download_posts
from platform_utils import platforms
import handler.db as db
from os import environ
from urllib import parse

app = Flask(__name__)
CORS(app)
api = Api(app)


class Keywords(Resource):

    def get(self):
        keywords = db.get_keywords()
        platform = platforms.copy()
        platform.append('All')
        return {
            'keyword': keywords,
            'platforms': platform
        }


class GetTotalSentimentValue(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('platform', type=str)
        parser.add_argument('term', type=str)
        args = parser.parse_args()
        term = parse.unquote(args['term'])
        stats = db.retrieve_post(term, args['platform'])
        if stats['total'] is 0:
            stats = download_posts(term, args['platform'])
        return stats


api.add_resource(Keywords, '/api/keywords')
api.add_resource(
    GetTotalSentimentValue,
    '/api/retrieveSentimentData'
)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(environ.get("PORT", 5000)),
        debug=True
    )
