def sort_even(l: list):
    
    l.sort()
    return [l[i] for i in range(len(l)) if i % 2 == 0]


