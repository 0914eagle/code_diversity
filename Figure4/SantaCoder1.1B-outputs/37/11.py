def sort_even(l: list):
    
    l.sort()
    for i in range(len(l) - 1):
        if i % 2 == 0:
            l[i], l[i + 1] = l[i + 1], l[i]
    return l


