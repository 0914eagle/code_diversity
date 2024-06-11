def sort_even(l: list):
    
    l_even = [l[i] for i in range(len(l)) if i % 2 == 0]
    l_even.sort()
    l_odd = [l[i] for i in range(len(l)) if i % 2 == 1]
    l_sorted = []
    for i in range(len(l)):
        if i % 2 == 0:
            l_sorted.append(l_even.pop(0))
        else:
            l_sorted.append(l_odd.pop(0))
    return l_sorted


