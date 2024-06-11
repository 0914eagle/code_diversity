def histogram(test):
    
    if test == '':
        return {}
    else:
        test = test.split()
        test = list(dict.fromkeys(test))
        test = dict.fromkeys(test, 0)
        for i in test:
            for j in test:
                if i == j:
                    test[i] += 1
        return test


