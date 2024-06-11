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
        max_value = max(hist.values())
        return {key: value for key, value in hist.items() if value == max_value}


