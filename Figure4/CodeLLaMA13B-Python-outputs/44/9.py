def change_base(x: int, base: int):
    
    if x == 0:
        return '0'
    if x < 0:
        return '-' + change_base(-x, base)
    if base < 2:
        raise ValueError("base must be greater than 1")
    if base > 10:
        raise ValueError("base must be less than 10")
    digits = '0123456789ABCDEF'
    result = ''
    while x > 0:
        result = digits[x % base] + result
        x = x // base
    return result


if