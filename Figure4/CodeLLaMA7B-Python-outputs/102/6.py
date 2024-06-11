def choose_num(x, y):
    
    if x % 2 == 0:
        if y % 2 == 0:
            if x < y:
                return max([i for i in range(x, y + 1) if i % 2 == 0])
            else:
                return -1
        else:
            return -1
    else:
        if y % 2 == 0:
            if x < y:
                return max([i for i in range(x, y + 1) if i % 2 == 0])
            else:
                return -1
        else:
            if x < y:
                return max([i for i in range(x, y + 1) if i % 2 == 0])
            else:
                return -1


print(choose_num(12, 15))
print(choose_num(13, 12))
