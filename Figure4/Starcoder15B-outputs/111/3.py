def histogram(test):
    
    # Your code here
    if test == '':
        return {}
    else:
        test = test.split()
        test_dict = {}
        for i in test:
            if i in test_dict:
                test_dict[i] += 1
            else:
                test_dict[i] = 1
        return test_dict


