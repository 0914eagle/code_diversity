def choose_num(x, y):
    
    # Your code here
    if x % 2 == 0:
        if x <= y:
            return x
        else:
            return -1
    else:
        x += 1
        if x <= y:
            return x
        else:
            return -1


