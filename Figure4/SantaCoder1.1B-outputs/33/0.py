def sort_third(l: list):
    
    l_copy = l[:]
    for i in range(len(l_copy)):
        if l_copy[i] % 3 != 0:
            l_copy[i], l_copy[i + 1] = l_copy[i + 1], l_copy[i]
    return l_copy


