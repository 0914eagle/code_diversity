def choose_num(x, y):
    
    if x % 2 != 0 or y % 2 != 0:
        return -1
    if x > y:
        return -1
    if x == y:
        return x
    if x > y:
        return -1
    if x % 2 == 0 and y % 2 == 0:
        if x > y:
            return -1
        if x == y:
            return x
        if x < y:
            return y
    if x % 2 != 0 and y % 2 != 0:
        if x > y:
            return -1
        if x == y:
            return x
        if x < y:
            return y
    if x % 2 != 0 and y % 2 == 0:
        if x > y:
            return -1
        if x == y:
            return x
        if x < y:
            return y
    if x % 2 == 0 and y % 2 != 0:
        if x > y:
            return -1
        if x == y:
            return x
        if x < y:
            return y


print(choose_num(12, 15))
print(choose_num(13, 12))
print(choose_num(12, 12))
print(choose_num(13, 13))
print(choose_num(14, 14))
print(choose_num(15, 15))
print(choose_num(16, 16))
print(choose_num(17, 17))
print(choose_num(18, 18))
print(choose_num(19, 19))
print(choose_num(20, 20))
print(choose_num(21, 21))
print(choose_num(22, 22))
print(choose_num(23, 23))
print(choose_num(24, 24))
print(choose_num(25, 25))
print(choose_num(26, 26))
