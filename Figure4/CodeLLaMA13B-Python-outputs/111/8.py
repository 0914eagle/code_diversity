def histogram(test):
    
    if test == '':
        return {}
    else:
        test = test.split()
        test = list(dict.fromkeys(test))
        hist = {}
        for i in test:
            hist[i] = test.count(i)
        hist = {k: v for k, v in hist.items() if v == max(hist.values())}
        return hist


