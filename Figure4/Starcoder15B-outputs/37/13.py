def sort_even(l: list):
    
    l_copy = l.copy()
    for i in range(0, len(l_copy), 2):
        l_copy[i] = sorted(l_copy[i::2])[i//2]
    return l_copy


