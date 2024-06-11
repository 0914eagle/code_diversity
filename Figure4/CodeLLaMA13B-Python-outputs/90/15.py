def next_smallest(lst):
    
    if len(lst) < 2:
        return None
    
    lst = sorted(lst)
    return lst[1]


