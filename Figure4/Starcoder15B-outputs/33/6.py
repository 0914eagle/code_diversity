def sort_third(l: list):
    
    l_copy = l.copy()
    for i in range(len(l)):
        if i % 3 == 0:
            l_copy[i] = sorted(l[i:i+3])
    return l_copy
