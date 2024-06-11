def unique_digits(x):
    
    return sorted(set(x) - set(map(lambda x: str(x), filter(lambda x: x % 2 == 0, x))))

