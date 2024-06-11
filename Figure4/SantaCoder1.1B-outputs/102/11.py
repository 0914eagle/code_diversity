def choose_num(x, y):
    
    if x < y:
        return -1
    if x == y:
        return x
    if x % 2 == 0:
        x = x / 2
    else:
        x = x + 1
    while x < y:
        if x % 2 == 0:
            x = x / 2
        else:
            x = x + 1
    return x


