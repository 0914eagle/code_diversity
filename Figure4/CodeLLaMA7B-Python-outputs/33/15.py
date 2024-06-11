def sort_third(l: list):
    
    l1 = []
    l2 = []
    for i in range(len(l)):
        if i % 3 == 0:
            l1.append(l[i])
        else:
            l2.append(l[i])
    l2.sort()
    l1.extend(l2)
    return l1


