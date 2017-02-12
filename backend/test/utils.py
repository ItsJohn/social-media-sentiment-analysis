from operator import itemgetter


def format_data(data):
    return sorted(
        data,
        key=itemgetter('text')
    )
