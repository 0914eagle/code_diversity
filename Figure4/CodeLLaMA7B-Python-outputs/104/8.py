def unique_digits(x):
    
    return sorted(list(set([int(i) for i in str(x) if int(i) % 2 != 0])))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
