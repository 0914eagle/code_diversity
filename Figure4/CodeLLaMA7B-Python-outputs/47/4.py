def median(l: list):
    
    l.sort()
    return l[len(l) // 2]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
