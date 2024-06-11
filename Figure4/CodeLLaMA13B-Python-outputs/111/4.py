def histogram(test):
    
    if not test:
        return {}
    else:
        hist = {}
        for i in test.split():
            if i not in hist:
                hist[i] = 1
            else:
                hist[i] += 1
        return hist


