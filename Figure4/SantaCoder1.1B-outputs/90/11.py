def next_smallest(lst):
    
    if not lst:
        return None
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        if lst[0] < lst[1]:
            return lst[0]
        else:
            return lst[1]
    if len(lst) == 3:
        if lst[0] < lst[1] and lst[0] < lst[2]:
            return lst[0]
        elif lst[1] < lst[0] and lst[1] < lst[2]:
            return lst[1]
        else:
            return lst[2]
    if len(lst) == 4:
        if lst[0] < lst[1] and lst[0] < lst[2] and lst[0] < lst[3]:
            return lst[0]
        elif lst[1] < lst[0] and lst[1] < lst[2] and lst[1] < lst[3]:
            return lst[1]
        elif lst[2] < lst[0] and lst[2] < lst[1] and lst[2] < lst[3]:
            return lst[2]
        else:
            return lst[3]
    if len(lst) == 5:
        if lst[0] < lst[1] and lst[0] < lst[2] and lst[0] < lst[3] and lst[0] < lst[4]:
            return lst[0]
        elif lst[1] < lst[0] and lst[1] < lst[2] and lst[1] < lst[3] and lst[1] < lst[4]:
            return lst[1]
        elif lst[2] < lst[0] and lst[2] < lst[1] and lst[2] < lst[3] and lst[2] < lst[4]:
            return lst[2]
        elif lst[3] < lst[0] and lst[3] < lst[1] and lst[3] < lst[2] and lst[3] < lst[4]:
            return lst[3]
        else:
            return lst[4]
    if len(lst) == 6:
        if lst[0] < lst[1] and lst[0] < lst[2] and lst[0] < lst[3] and