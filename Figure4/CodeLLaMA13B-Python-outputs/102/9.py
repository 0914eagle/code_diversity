def choose_num(x, y):
    
    if x <= 0 or y <= 0:
        return -1
    if x > y:
        x, y = y, x
    if y % 2 == 1:
        y -= 1
    if x == y:
        if x % 2 == 0:
            return x
        else:
            return -1
    return y


