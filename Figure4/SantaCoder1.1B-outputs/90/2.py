def next_smallest(lst):
    
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0]
    else:
        return min(lst[1:])


