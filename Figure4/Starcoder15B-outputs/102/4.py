def choose_num(x, y):
    
    # TODO: write your code here
    if x > y:
        return -1
    if x % 2 == 0:
        return x
    else:
        return choose_num(x + 1, y)

