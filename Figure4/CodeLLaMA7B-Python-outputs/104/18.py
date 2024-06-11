def unique_digits(x):
    
    return sorted(list(set([x for x in x if not any(map(lambda y: y % 2 == 0, map(int, str(x))))])))


if __name__