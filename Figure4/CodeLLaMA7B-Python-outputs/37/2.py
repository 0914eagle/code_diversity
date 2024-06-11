def sort_even(l: list):
    
    l1 = []
    l2 = []
    for i in l:
        if i % 2 == 0:
            l1.append(i)
        else:
            l2.append(i)
    l1.sort()
    l2.sort()
    l3 = []
    for i in range(len(l)):
        if i % 2 == 0:
            l3.append(l1[i // 2])
        else:
            l3.append(l2[i // 2])
    return l3


