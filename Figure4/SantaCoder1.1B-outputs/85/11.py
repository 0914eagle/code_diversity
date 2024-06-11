def add(lst):
    
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + add(lst[1:])


