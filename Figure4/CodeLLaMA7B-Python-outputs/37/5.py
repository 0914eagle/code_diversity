def sort_even(l: list):
    
    l2 = []
    for i in range(len(l)):
        if i % 2 == 0:
            l2.append(l[i])
    l2.sort()
    for i in range(len(l)):
        if i % 2 == 1:
            l[i] = l2[i // 2]
    return l


if __name__ == "__main__":
    import doctest

    doctest.testmod()
