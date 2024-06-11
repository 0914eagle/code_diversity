def histogram(test):
    
    d = {}
    for c in test.lower():
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d


