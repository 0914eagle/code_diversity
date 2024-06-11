def next_smallest(lst):
    
    if not lst:
        return None
    else:
        lst.sort()
        return lst[1]


