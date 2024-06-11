def sort_third(l: list):
    
    l_copy = l[:]
    for i in range(len(l_copy)):
        if l_copy[i] % 3 == 0:
            l_copy[i] = l_copy[i] // 3
    l_copy.sort()
    for i in range(len(l_copy)):
        if l_copy[i] % 3 == 0:
            l_copy[i] = l_copy[i] * 3
    return l_copy


