def choose_num(x, y):
    
    if x <= 0 or y <= 0:
        return -1
    if x > y:
        return -1
    if x % 2 == 1:
        x += 1
    if y % 2 == 1:
        y -= 1
    if x > y:
        return -1
    if y - x <= 1:
        return y
    return y - 1


