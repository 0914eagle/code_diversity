def choose_num(x, y):
    
    if x <= 0 or y <= 0:
        return -1
    if x > y:
        return -1
    if x == y:
        return x
    if x % 2 == 0:
        return x
    if y % 2 == 0:
        return y
    if (x + 1) % 2 == 0:
        return x + 1
    if (y - 1) % 2 == 0:
        return y - 1
    return -1


