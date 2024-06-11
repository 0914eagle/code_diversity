def unique_digits(x):
    
    return sorted(set(x) - set(i for i in x if '2' in str(i) or '4' in str(i) or '6' in str(i) or '8' in str(i)))


if __name__