def median(l: list):
    
    l.sort()
    n = len(l)
    if n % 2 == 1:
        return l[n // 2]
    else:
        return (l[n // 2] + l[n // 2 - 1]) / 2


if __name__ == "__main__":
    import doctest

    doctest.