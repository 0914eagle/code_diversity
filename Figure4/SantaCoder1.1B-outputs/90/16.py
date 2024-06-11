def next_smallest(lst):
    
    if len(lst) == 0:
        return None
    else:
        lst.sort()
        return lst[1]

