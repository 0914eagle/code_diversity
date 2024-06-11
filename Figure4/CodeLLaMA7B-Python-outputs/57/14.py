def monotonic(l: list):
    
    return l == sorted(l) or l == sorted(l, reverse=True)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
