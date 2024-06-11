def unique_digits(x):
    
    return sorted([i for i in x if not any(d in str(i) for d in "02468")])


if __name__ ==