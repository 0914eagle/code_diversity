def sort_even(l: list):
    
    l.sort()
    for i in range(len(l) - 1, 0, -2):
        if l[i] == l[i - 1]:
            l[i - 1], l[i] = l[i], l[i - 1]
    return l


