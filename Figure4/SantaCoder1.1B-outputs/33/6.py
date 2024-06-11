def sort_third(l: list):
    
    l_copy = l.copy()
    for i in range(len(l)):
        if l[i] % 3 == 0:
            l_copy[i] = l[i]
    return l_copy


