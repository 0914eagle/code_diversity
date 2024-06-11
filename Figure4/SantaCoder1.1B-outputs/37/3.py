def sort_even(l: list):
    
    l.sort()
    l_odd = []
    for i in range(len(l)):
        if i % 2 == 0:
            l_odd.append(l[i])
    return l_odd


