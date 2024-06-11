def sort_third(l: list):
    
    l.sort()
    l_new = []
    for i in range(len(l)):
        if i % 3 == 0:
            l_new.append(l[i])
    return l_new


