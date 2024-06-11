def choose_num(x, y):
    
    if x < y:
        return -1
    for i in range(x, y + 1):
        if is_even(i):
            return i
    return -1


