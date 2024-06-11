def sort_third(l: list):
    
    l_copy = l.copy()
    l_copy[::3] = sorted(l[::3])
    return l_copy


if __name__ == "__main__":
    import doctest

    doctest.testmod()