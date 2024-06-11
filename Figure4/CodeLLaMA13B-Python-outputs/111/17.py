def histogram(test):
    
    if test == "":
        return {}
    else:
        test = test.split()
        test = list(dict.fromkeys(test))
        test = dict.fromkeys(test, 0)
        for i in test:
            for j in test:
                if i == j:
                    test[i] += 1
        test = dict(sorted(test.items(), key=lambda item: item[1], reverse=True))
        return test


print(histogram("a b c"))
print(histogram("a b b a"))
print(histogram("a b c a b"))
print(histogram("b b b b a"))
print(histogram(""))
