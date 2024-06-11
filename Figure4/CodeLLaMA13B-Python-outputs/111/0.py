def histogram(test):
    
    if test == '':
        return {}
    else:
        hist = {}
        for i in test.split():
            if i in hist:
                hist[i] += 1
            else:
                hist[i] = 1
        max_value = max(hist.values())
        return {k: v for k, v in hist.items() if v == max_value}


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}, "a b c"
    assert histogram('a b b a') == {'a': 2, 'b': 2}, "a b b a"
    assert histogram('a b c a b') == {'a': 2, 'b': 2}, "a b c a b"
    assert histogram('b b b b a') == {'b': 4}, "b b b b a"
    assert histogram('') == {}, "Let's try with an empty string"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
