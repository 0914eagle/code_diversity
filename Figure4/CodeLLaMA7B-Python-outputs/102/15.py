def choose_num(x, y):
    
    if x % 2 != 0:
        x += 1
    if y % 2 != 0:
        y -= 1
    for i in range(x, y + 1, 2):
        if i % 2 == 0:
            return i
    return -1


print(choose_num(12, 15))
print(choose_num(13, 12))
