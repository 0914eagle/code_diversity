def sort_third(l: list):
    
    l.sort()
    return [l[i] for i in range(len(l)) if i % 3 != 0]


