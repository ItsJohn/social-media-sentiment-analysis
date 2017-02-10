from time import gmtime


HALF_HOUR = 30
HOUR = 60


def get_hour():
    """ Retrieves the current hour """
    return gmtime().tm_hour


def get_minute():
    return gmtime().tm_min


def check_hour(hour):
    """ Checks if an hour has past since the hour that has been passed in """
    return True if hour < get_hour() else False


def check_minute(minute):
    """ Checks if an half an hour has past since
        the minute that has been passed in """
    return True if (minute + HALF_HOUR) % HOUR == get_minute() else False
