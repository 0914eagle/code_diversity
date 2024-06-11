def unique_digits(x):
    
    return sorted([i for i in x if not any(map(lambda x: int(x) % 2 == 0, str(i)))])

if