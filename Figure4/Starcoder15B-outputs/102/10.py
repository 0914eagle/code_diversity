def choose_num(x, y):
    
    # your code here
    if x > y:
        return -1
    elif x % 2 == 0:
        return x
    else:
        return choose_num(x + 1, y)

#