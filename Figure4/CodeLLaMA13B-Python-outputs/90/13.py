def next_smallest(lst):
    
    if len(lst) == 0 or len(lst) == 1:
        return None
    lst.sort()
    return lst[1]


