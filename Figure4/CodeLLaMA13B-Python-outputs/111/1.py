def histogram(test):
    
    if test == "":
        return {}
    else:
        test = test.split()
        test = list(dict.fromkeys(test))
        test = dict.fromkeys(test, 0)
        for i in test:
            test[i] = test[i] + test.get(i, 0)
        return test


print(histogram("a b c"))
print(histogram("a b b a"))
print(histogram("a b c a b"))
print(histogram("b b b b a"))
print(histogram(""))
