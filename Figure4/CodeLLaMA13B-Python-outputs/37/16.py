def sort_even(l: list):
    
    # Your code here
    l_copy = l.copy()
    for i in range(0, len(l), 2):
        l[i] = l_copy[i + 1]
    l.sort()
    return l


if __name__ == "__main__":
    import doctest

    doctest.testmod()
