def common(l1: list, l2: list):
    
    return sorted(set(l1) & set(l2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
