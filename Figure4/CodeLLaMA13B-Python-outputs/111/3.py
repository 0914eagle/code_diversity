def histogram(test):
    
    if not test:
        return {}
    else:
        test = test.split()
        hist = {}
        for i in test:
            if i in hist:
                hist[i] += 1
            else:
                hist[i] = 1
        max_val = max(hist.values())
        return {k: v for k, v in hist.items() if v == max_val}


print(histogram('a b c'))
print(histogram('a b b a'))
print(histogram('a b c a b'))
print(histogram('b b b b a'))
print(histogram(''))
