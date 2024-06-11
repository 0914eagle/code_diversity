def sort_even(l: list):
    
    l_even = []
    for i in range(len(l)):
        if i % 2 == 0:
            l_even.append(l[i])
    l_even.sort()
    l_sorted = []
    for i in range(len(l)):
        if i % 2 == 0:
            l_sorted.append(l_even[i//2])
        else:
            l_sorted.append(l[i])
    return l_sorted

