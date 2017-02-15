from operator import itemgetter


def format_data(data):
    return sorted(
        data,
        key=itemgetter('text')
    )


def second_element(element):
    return element[1]


def sort_tuple_list(data):
    return sorted(data, key=second_element)
