def histogram(test):
    
    # Your code here
    # Your code here
    if test == '':
        return {}
    else:
        test = test.split()
        test = Counter(test)
        return test


# +
# histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
# histogram('a b b a') == {'a': 2, 'b': 2}
# histogram('a b c a b') == {'a': 2, 'b': 2}
# histogram('b b b b a') == {'b':