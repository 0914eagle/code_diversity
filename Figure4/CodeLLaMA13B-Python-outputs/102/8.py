def choose_num(x, y):
    
    if x <= 0 or y <= 0:
        return -1
    if x > y:
        x, y = y, x
    if y % 2 == 1:
        y -= 1
    if x == y:
        return x
    if x % 2 == 1:
        x += 1
    if x <= y:
        return y
    return -1


