def sort_third(l: list):
    
    l_copy = l.copy()
    for i in range(len(l_copy)):
        if i % 3 == 0:
            l_copy[i] = l[i]
    l_copy.sort()
    return l_copy


