def histogram(test):
    
    histogram = {}
    for letter in test.split():
        if letter in histogram:
            histogram[letter] += 1
        else:
            histogram[letter] = 1
    return histogram


