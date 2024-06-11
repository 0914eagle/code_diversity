def histogram(test):
    
    if test == '':
        return {}
    else:
        test = test.split()
        hist = {}
        for i in test:
            if i not in hist:
                hist[i] = 1
            else:
                hist[i] += 1
        max_value = max(hist.values())
        return {key: value for key, value in hist.items() if value == max_value}


print(histogram('a b c'))
print(histogram('a b b a'))
print(histogram('a b c a b'))
print(histogram('b b b b a'))
print(histogram(''))
