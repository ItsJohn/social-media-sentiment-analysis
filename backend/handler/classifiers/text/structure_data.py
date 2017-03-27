from handler.classifiers.text.utils import process_text


def open_files(category: str, the_file: str) -> tuple:
    all_data = []
    categories = []
    with open(the_file) as fh:
        for data in fh:
            words = process_text(data[:-1])
            if words:
                all_data.append(words)
                categories.append(category)

    return all_data, categories


def getData(**kwargs) -> list:
    """
        This is used to create the categories for the classifiers
        Example: getData(positive='PATH_TO_FILE', negative='PATH_TO_FILE')
    """
    global word_features
    all_data = {
        'data': [],
        'category': []
    }
    print('Loading data from file...')
    for category, file_name in kwargs.items():
        data, category = open_files(category, file_name)
        all_data['data'].extend(data)
        all_data['category'].extend(category)

    return all_data
