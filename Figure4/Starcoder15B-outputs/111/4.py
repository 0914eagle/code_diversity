def histogram(test):
    
    # your code here
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
/python/python-basics/python-basics-1/01_hello_world.py
#