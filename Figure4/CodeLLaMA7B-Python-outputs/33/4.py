def sort_third(l: list):
    
    l = l[:]
    for i in range(0, len(l), 3):
        l[i] = l[i + 2]
    l.sort()
    for i in range(0, len(l), 3):
        l[i] = l[i + 1]
    return l


if __name__ == "__main__":
    import doctest

    doctest.testmod()
