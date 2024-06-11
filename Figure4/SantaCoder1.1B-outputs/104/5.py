def unique_digits(x):
    
    return sorted(set(x) - set(map(int, str(x))))


