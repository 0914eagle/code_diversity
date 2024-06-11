def choose_num(x, y):
    
    if x % 2 == 1:
        x += 1
    if y % 2 == 1:
        y -= 1
    for i in range(x, y+1, 2):
        if i > y:
            return -1
        else:
            return i


print(choose_num(12, 15))
print(choose_num(13, 12))
