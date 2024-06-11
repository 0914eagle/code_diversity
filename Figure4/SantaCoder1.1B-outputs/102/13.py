def choose_num(x, y):
    
    if x < 0 or y < 0:
        return -1
    if x == y:
        return x
    if x % 2 == 0:
        x = x / 2
        y = y / 2
    else:
        x = x + 1
        y = y / 2
    while x < y:
        x = x + 1
    return x


