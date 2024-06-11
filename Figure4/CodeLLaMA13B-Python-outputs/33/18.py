def sort_third(l: list):
    
    l[:] = [l[i] if i % 3 == 0 else sorted(l[i:i + 3]) for i in range(0, len(l), 3)]
    return l


if __name__ == "__main__":
    import doctest
    doctest.testmod()
