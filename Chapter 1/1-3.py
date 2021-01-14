def minmax(data):
    min_ = data[0]
    max_ = data[0]
    for datum in data:
        if datum < min_:
            min_ = datum
        elif datum > max_:
            max_ = datum
    return min_, max_