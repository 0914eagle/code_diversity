def sort_even(l: list):
    
    l1 = []
    l2 = []
    for i in range(len(l)):
        if i % 2 == 0:
            l1.append(l[i])
        else:
            l2.append(l[i])
    l2.sort()
    for i in range(len(l1)):
        l[i * 2] = l2[i]
    return l


if __name__ == "__main__":
    import doctest

    doctest.testmod()
