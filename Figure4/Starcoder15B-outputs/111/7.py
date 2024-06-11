def histogram(test):
    
    if test == '':
        return {}
    else:
        test = test.split()
        test = Counter(test)
        return test

#print(histogram('a b c'))
#print(histogram('a b