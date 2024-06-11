def histogram(test):
    
    # Your code here
    # return {}
    # return test
    if not test:
        return {}
    count = {}
    for letter in test:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count

