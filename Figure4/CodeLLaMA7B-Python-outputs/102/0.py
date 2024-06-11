def choose_num(x, y):
    
    if x % 2 != 0 or y % 2 != 0:
        return -1
    if x > y:
        return -1
    if x == y:
        return x
    if x < y:
        for i in range(x, y+1):
            if i % 2 == 0:
                return i


print(choose_num(12, 15))
print(choose_num(13, 12))
