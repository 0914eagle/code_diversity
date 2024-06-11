def sort_third(l: list):
    
    l.sort()
    for i in range(len(l)):
        if i % 3 == 0:
            l[i], l[i + 1], l[i + 2] = l[i + 2], l[i + 1], l[i]
    return l


