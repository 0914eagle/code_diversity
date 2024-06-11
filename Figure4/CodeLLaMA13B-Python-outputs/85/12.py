def add(lst):
    
    if len(lst) == 0:
        return 0
    else:
        if lst[0] % 2 == 0 and lst[0] % 2 == 0:
            return lst[0] + add(lst[2:])
        else:
            return add(lst[1:])


if