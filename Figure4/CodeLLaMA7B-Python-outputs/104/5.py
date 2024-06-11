def unique_digits(x):
    
    return sorted(filter(lambda x: not any(map(lambda y: y % 2 == 0, map(int, str(x)))), x))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
