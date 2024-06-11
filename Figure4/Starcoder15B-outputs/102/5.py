def choose_num(x, y):
    
    if x % 2 == 0:
        if x <= y:
            return x
        else:
            return -1
    else:
        if x + 1 <= y:
            return x + 1
        else:
            return -1

