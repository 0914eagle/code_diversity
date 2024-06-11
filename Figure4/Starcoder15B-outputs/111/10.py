def histogram(test):
    
    if test == '':
        return {}
    else:
        test = test.split()
        test = Counter(test)
        return test

print(histogram('a b c'))
print(histogram('a b b a'))
print(histogram('a b c a b'))
print(histogram('b b b b a'))
print(histogram(''))
/python/python_basics/python_basics_1.py
#