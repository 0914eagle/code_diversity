def sort_third(l: list):
    
    l_copy = l.copy()
    for i in range(len(l_copy)):
        if i % 3 == 0:
            l_copy[i] = sorted(l_copy[i:i+3])
    return l_copy


