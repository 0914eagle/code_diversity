def choose_num(x, y):
    
    if x > y:
        return -1
    elif x % 2 == 1:
        x += 1
    if y % 2 == 1:
        y -= 1
    if x > y:
        return -1
    else:
        return y

print(choose_num(12, 15))
print(choose_num(13, 12))
print(choose_num(12, 12))
print(choose_num(12, 13))
print(choose_num(13, 14))
print(choose_num(14, 12))
print(choose_num(14, 13))
print(choose_num(13, 13))
print(choose_num(13, 14))
print(choose_num(14, 14))
print(choose_num(14, 15))
print(choose_num(15, 14))
print(choose_num(15, 15))
print(choose_num(15, 16))
print(choose_num(16, 15))
print(choose_num(16, 16))
print(choose_num(16, 17))
print(choose_num(17, 16))
print(choose_num(17, 17))
print(choose_num(17, 18))
print(choose_num(18, 17))
print(choose_num(18, 18))
print(choose_num(18, 19))
print(choose_num(19, 18))
print(choose_num(19, 19))
print(choose_num(19, 20))
print(choose_num(20, 19))
print(choose_num(20, 20))
print(choose_num(20, 21))
print(choose_num(21, 20))
print(choose_num(21, 21))
print(choose_num(21, 