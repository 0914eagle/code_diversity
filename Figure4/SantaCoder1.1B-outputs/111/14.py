def histogram(test):
    
    # Your code here
    d = {}
    for i in test.split():
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

