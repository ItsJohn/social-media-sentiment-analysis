from platform_utils import platforms
from handler.db import insert_data
from handler.db_utils import format_data
from handler.twitter.download_tweets import retrieve_tweets
from handler.twitter.twitter_api import query_twitter_for_tweets
from handler.twitter.tweet_utils import extract_tweet
from handler.classifiers.sentiment import classify_data


def choose_platform():
    """ When running `./run download` this
        asks which platform to download from """
    if len(platforms) == 1:
        chosen_platform = platforms[0]
    else:
        for i, platform in enumerate(platforms):
            print(i + 1, platform)
        choice = int(input("Select a platform to download from: "))
        chosen_platform = platforms[choice - 1]
    return chosen_platform


def continuous_download():
    """ Implements how to continuous download from the chosen platform """
    chosen_platform = choose_platform()
    # TODO: Add platforms download here
    if chosen_platform is 'Twitter':
        retrieve_tweets()


def download_posts(term: str, platform: str) -> list:
    """ When no posts have been retieved from the database,
        This will download straight from that platform
        Default download is from Twitter
    """
    # TODO: Add an if statement for new platform, set data to formatted list
    if platform == 'Twitter':
        data = extract_tweet(
            query_twitter_for_tweets(term, auth='search')['statuses'],
            term
        )
    else:
        # Default download from Twitter
        data = extract_tweet(
            query_twitter_for_tweets(term, auth='search')['statuses'],
            term
        )
    stats = classify_data(data)
    insert_data(stats)
    return format_data(stats)


if __name__ == "__main__":
    continuous_download()
