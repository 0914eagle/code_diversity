def sort_even(l: list):
    
    l_even = [l[i] for i in range(0, len(l), 2)]
    l_even.sort()
    l_odd = [l[i] for i in range(1, len(l), 2)]
    l_new = []
    for i in range(len(l)):
        if i % 2 == 0:
            l_new.append(l_even[i // 2])
        else:
            l_new.append(l_odd[i // 2])
    return l_new


