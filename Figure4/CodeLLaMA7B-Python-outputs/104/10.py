def unique_digits(x):
    
    return sorted(set(x) - set(filter(lambda x: x % 2 == 0, x)))
