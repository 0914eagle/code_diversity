def sort_even(l: list):
    
    even_sorted = sorted(l[::2])
    l[::2] = even_sorted
    return l


if __name__ == "__main__":
    import doctest

    doctest.testmod()
