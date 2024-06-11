def sort_even(l: list):
    
    l_odd = []
    l_even = []
    for i in range(len(l)):
        if i % 2 == 0:
            l_even.append(l[i])
        else:
            l_odd.append(l[i])
    l_odd.sort()
    l_even.sort()
    l_even.extend(l_odd)
    return l_even


