def unique_digits(x):
    
    return sorted(list(set(x) - set(map(int, str(x)))))

