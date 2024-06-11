def histogram(test):
    
    if test == '':
        return {}
    else:
        test_list = test.split()
        test_dict = {}
        for i in test_list:
            if i in test_dict:
                test_dict[i] += 1
            else:
                test_dict[i] = 1
        max_value = max(test_dict.values())
        return {key: value for key, value in test_dict.items() if value == max_value}


print(histogram('a b c'))
print(histogram('a b b a'))
print(histogram('a b c a b'))
print(histogram('b b b b a'))
print(histogram(''))
