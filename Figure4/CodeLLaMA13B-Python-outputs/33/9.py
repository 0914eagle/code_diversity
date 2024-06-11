def sort_third(l: list):
    
    l[:] = [x for i, x in enumerate(l) if i % 3 == 0] + sorted([x for i, x in enumerate(l) if i % 3 != 0])
    return l


if __name__ == "__main__":
    import doctest
    doctest.testmod()
