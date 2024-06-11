def unique_digits(x):
    
    return sorted([x for x in x if not any(d in str(x) for d in '02468')])


if