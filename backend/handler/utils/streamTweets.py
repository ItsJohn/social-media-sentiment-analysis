from tweepy import Stream
from tweepy.streaming import StreamListener

from twitter_api import oAuth
from tweet_utils import extract_tweet, format_json


# override StreamListener to add logic to on_status
class listener(StreamListener):
    def on_status(self, tweet):
        format_json(tweet)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False


myStream = Stream(auth=oAuth(), listener=listener())
myStream.filter(track=['python'], async=True)
