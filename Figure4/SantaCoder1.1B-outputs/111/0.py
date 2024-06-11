def histogram(test):
    
    counts = {}
    for letter in test.split():
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts


