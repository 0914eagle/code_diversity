def unique_digits(x):
    
    return sorted(list(set([x for x in x if not '2' in str(x) and not '4' in str(x) and not '6' in str(x) and not '8' in str(x)])))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
