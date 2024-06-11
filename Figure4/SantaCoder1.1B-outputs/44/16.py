def change_base(x: int, base: int):
    
    if base < 2:
        raise ValueError("base must be greater than 1")
    if base > 36:
        raise ValueError("base must be less than 36")
    if x < 0:
        raise ValueError("x must be greater than 0")
    if x == 0:
        return "0"
    if x == 1:
        return "1"
    if x == 2:
        return "10"
    if x == 3:
        return "100"
    if x == 4:
        return "1000"
    if x == 5:
        return "10000"
    if x == 6:
        return "100000"
    if x == 7:
        return "1000000"
    if x == 8:
        return "10000000"
    if x == 9:
        return "100000000"
    if x == 10:
        return "1000000000"
    if x == 11:
        return "100000000000"
    if x == 12:
        return "1000000000000"
    if x == 13:
        return "10000000000000"
    if x == 14:
        return "100000000000000"
    if x == 15:
        return "1000000000000000"
    if x == 16:
        return "10000000000000000"
    if x == 17:
        return "100000000000000000"
    if x == 18:
        return "1000000000000000000"
    if x == 19:
        return "10000000000000000000"
    if x == 20:
        return "100000000000