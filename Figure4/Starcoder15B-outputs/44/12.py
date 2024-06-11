def change_base(x: int, base: int):
    
    if x == 0:
        return '0'
    else:
        return change_base(x // base, base) + str(x % base)

