def unique_digits(x):
    
    return [x for x in x if not any(int(i) % 2 == 0 for i in str(x))]


