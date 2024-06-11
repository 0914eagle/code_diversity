def monotonic(l: list):
    
    return all(x <= y for x, y in zip(l, l[1:])) or all(x >= y for x, y in zip(l, l[1:]))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
