def unique_digits(x):
    
    return sorted(list(set(x) - set([i for i in x if not i % 2])))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
