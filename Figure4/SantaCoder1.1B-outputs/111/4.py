def histogram(test):
    
    d = {}
    for letter in test.split():
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    return d


