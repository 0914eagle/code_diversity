def sort_third(l: list):
    
    l = l.copy()
    for i in range(len(l)):
        if i % 3 == 0:
            l[i] = sorted(l[i:i+3])[1]
    return l


if __name__ == "__main__":
    import doctest
    doctest