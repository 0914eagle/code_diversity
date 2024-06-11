def unique_digits(x):
    
    return sorted(set(x) - set(map(str, range(10))))

