def histogram(test):
    
    if not test:
        return {}
    counts = {}
    for letter in test.split():
        counts[letter] = counts.get(letter, 0) + 1
    return counts


