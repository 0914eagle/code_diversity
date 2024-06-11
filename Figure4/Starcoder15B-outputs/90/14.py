def next_smallest(lst):
    
    if len(lst) < 2:
        return None
    else:
        return sorted(lst)[1]

#