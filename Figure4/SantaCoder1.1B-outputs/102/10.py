def choose_num(x, y):
    
    if x < y:
        return -1
    if x == y:
        return x
    if x % 2 == 0:
        return x + 1
    else:
        return x + 2


