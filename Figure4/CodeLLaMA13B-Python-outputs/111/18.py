def histogram(test):
    
    if test == "":
        return {}
    else:
        hist = {}
        for i in test.split():
            if i in hist:
                hist[i] += 1
            else:
                hist[i] = 1
        return hist


