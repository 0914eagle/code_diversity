def choose_num(x, y):
    
    if x % 2 == 0:
        if y % 2 == 0:
            if x < y:
                return y
            else:
                return x
        else:
            return -1
    else:
        if y % 2 == 0:
            return y
        else:
            return -1


print(choose_num(12, 15))
print(choose_num(13, 12))
