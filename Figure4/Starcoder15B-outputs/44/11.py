def change_base(x: int, base: int):
    
    if x == 0:
        return '0'
    if x < 0:
        return '-' + change_base(-x, base)
    digits = '0123456789'
    if x < base:
        return digits[x]
    return change_base(x // base, base) + digits[x % base]


