def sort_third(l: list):
    
    l_copy = l.copy()
    for i in range(0, len(l), 3):
        l_copy[i] = l[i + 2]
    l_copy.sort()
    for i in range(0, len(l), 3):
        l[i + 2] = l_copy[i]
    return l


if __name__ == "__main__":
    import doctest

    doctest.testmod