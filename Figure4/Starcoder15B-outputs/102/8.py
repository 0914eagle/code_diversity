def choose_num(x, y):
    
    # Your code here
    if x % 2 == 0:
        return x
    elif y % 2 == 0:
        return y
    elif x % 2 != 0:
        x += 1
        return x
    elif y % 2 != 0:
        y -= 1
        return y
    else:
        return -1

#