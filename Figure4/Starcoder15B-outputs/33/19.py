def sort_third(l: list):
    
    l_copy = l[:]
    for i in range(len(l)):
        if i % 3 == 0:
            l_copy[i] = sorted(l_copy[i:i+3])
    return l_copy

