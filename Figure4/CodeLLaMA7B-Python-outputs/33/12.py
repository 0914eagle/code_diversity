def sort_third(l: list):
    
    l_copy = l.copy()
    for i in range(0, len(l), 3):
        l_copy[i] = sorted(l)[i]
    return l_copy


