def choose_num(x, y):
    
    if x < 0 or y < 0:
        return -1
    if x > y:
        return -1
    if x == y:
        return x
    for i in range(x, y + 1):
        if i % 2 == 0:
            return i
    return -1


