def histogram(test):
    
    if not test:
        return {}
    d = {}
    for c in test.split():
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d


