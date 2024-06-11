def sort_third(l: list):
    
    l2 = []
    for i in range(len(l)):
        if i % 3 != 0:
            l2.append(l[i])
    l2.sort()
    l3 = []
    for i in range(len(l)):
        if i % 3 == 0:
            l3.append(l2[i // 3])
        else:
            l3.append(l[i])
    return l3


if __name__ == "__main__":
    import doctest

    doctest.testmod()
