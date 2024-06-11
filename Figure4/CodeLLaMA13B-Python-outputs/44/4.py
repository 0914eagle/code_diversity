def change_base(x: int, base: int):
    
    if x == 0:
        return '0'
    if x < 0:
        return '-' + change_base(-x, base)
    result = ''
    while x > 0:
        result = str(x % base) + result
        x //= base
    return result


