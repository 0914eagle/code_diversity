def unique_digits(x):
    
    return sorted([i for i in x if not any(str(i).count(j) for j in '02468')])


if __name