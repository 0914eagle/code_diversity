def change_base(x: int, base: int):
    
    if base < 2:
        raise ValueError("base must be greater than 1")
    if base > 36:
        raise ValueError("base must be less than 36")
    if base == 10:
        return str(x)
    if base == 2:
        return str(x).zfill(2)
    if base == 3:
        return str(x).zfill(3)
    if base == 4:
        return str(x).zfill(4)
    if base == 5:
        return str(x).zfill(5)
    if base == 6:
        return str(x).zfill(6)
    if base == 7:
        return str(x).zfill(7)
    if base == 8:
        return str(x).zfill(8)
    if base == 9:
        return str(x).zfill(9)
    if base == 10:
        return str(x).zfill(10)
    if base == 11:
        return str(x).zfill(11)
    if base == 12:
        return str(x).zfill(12)
    if base == 13:
        return str(x).zfill(13)
    if base == 14:
        return str(x).zfill(14)
    if base == 15:
        return str(x).zfill(15)
    if base == 16:
        return str(x).zfill(16)
    if base == 17:
        return str(x).zfill(17)
    if base == 18:
        return str(x).zfill(18)
    if base == 19:
        return str(x).zfill(19)
    if base == 20:
        return str(x).zfill(20)
    if base == 21:
        return str(x).zfill(21)
    if base == 22:
        return str(x).zfill(22)
    if base == 23:
        return str(x).zfill(23)
    if base == 24:
        return str(x).zfill(24)
    if base == 25:
        return str(x).zfill(25)
    if base == 26:
        return str(x).zfill(26