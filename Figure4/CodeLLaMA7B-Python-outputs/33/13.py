def sort_third(l: list):
    
    return sorted(l, key=lambda x: x % 3)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
