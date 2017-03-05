from handler.classifiers.sentiment import find_sentiment


# TODO: Add new platform here
platforms = [
    'Twitter'
]


def classify_post():
    """ Call this to classify new posts
        Used for when reaching rate limit to maximise efficiency
        eg.
            from platform_utils import classify_post
            classify_post()
    """
    find_sentiment()
