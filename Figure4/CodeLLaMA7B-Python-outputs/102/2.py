def choose_num(x, y):
    
    if x % 2 == 0:
        if y % 2 == 0:
            if x > y:
                return -1
            else:
                for i in range(x, y + 1, 2):
                    if i % 2 == 0:
                        return i
        else:
            if x > y:
                return -1
            else:
                for i in range(x, y + 1, 2):
                    if i % 2 == 0:
                        return i
    else:
        if y % 2 == 0:
            if x > y:
                return -1
            else:
                for i in range(x, y + 1, 2):
                    if i % 2 == 0:
                        return i
        else:
            if x > y:
                return -1
            else:
                for i in range(x, y + 1, 2):
                    if i % 2 == 0:
                        return i


print(choose_num(12, 15))
print(choose_num(13, 12))
