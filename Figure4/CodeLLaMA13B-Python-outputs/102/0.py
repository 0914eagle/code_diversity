def choose_num(x, y):
    
    if x > y:
        return -1
    if x % 2 == 0:
        if x <= y:
            return x
    else:
        x += 1
        if x <= y:
            return x
    for i in range(x, y + 1, 2):
        return i
    return -1


