import pickle


def save_this(path: str, content):
    with open(path, 'wb') as fh:
        pickle.dump(content, fh)


def open_this(path: str):
    with open(path, 'rb') as fh:
        content = pickle.load(fh)
    return content
