def histogram(test):
    
    if test == '':
        return {}
    else:
        test = test.split()
        d = {}
        for i in test:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        max_value = max(d.values())
        return {k: v for k, v in d.items() if v == max_value}


print(histogram('a b c'))
print(histogram('a b b a'))
print(histogram('a b c a b'))
print(histogram('b b b b a'))
print(histogram(''))
