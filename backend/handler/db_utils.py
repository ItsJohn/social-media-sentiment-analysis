def format_data(data: list) -> dict:
    """ Translates data into JSON  """
    pos_count = 0
    neg_count = 0
    new_content = []
    coordinates = []
    for content in data:
        if content['sentiment'] == 'positive':
            pos_count = pos_count + 1
        else:
            neg_count = neg_count + 1
        if 'coordinates' in content:
            coordinates.append({
                'lng': content['coordinates'][0],
                'lat': content['coordinates'][1]
            })
        new_content.append(content)

    return {
        'total': pos_count + neg_count,
        'sentiment': {
            'positive': pos_count,
            'negative': neg_count
        },
        'coordinates': coordinates,
        'tweets': new_content
    }
