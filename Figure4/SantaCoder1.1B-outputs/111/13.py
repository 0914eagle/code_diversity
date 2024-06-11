def histogram(test):
    
    if not test:
        return {}
    test = test.lower()
    counts = {}
    for letter in test:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts


