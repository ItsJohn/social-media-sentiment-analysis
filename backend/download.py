from handler.db import insert_data
from handler.classifiers.sentiment import classify_data
from platforms.platform_utils import platforms
from platforms.platform_utils import download_continuously
from platforms.platform_utils import download_single_set_of_posts


def choose_platform():
    """ Implements how to continuous download from the chosen platform """
    if len(platforms) == 1:
        chosen_platform = platforms[0]
    else:
        for i, platform in enumerate(platforms):
            print(i + 1, platform)
        choice = int(input("Select a platform to download from: "))
        chosen_platform = platforms[choice - 1]
    download_continuously(chosen_platform)


def download_posts(term: str, platform: str) -> list:
    """ When no posts have been retieved from the database,
        This will download straight from that platform
        Default download is from Twitter
    """
    data = download_single_set_of_posts(term, platform)
    stats = classify_data(data)
    insert_data(stats)
    for posts in stats:
        if '_id' in posts:
            del posts['_id']
    return stats


if __name__ == "__main__":
    choose_platform()
