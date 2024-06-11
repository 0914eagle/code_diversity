def sort_even(l: list):
    
    l_copy = l[:]
    for i in range(0, len(l), 2):
        l_copy[i] = sorted(l)[i]
    return l_copy


