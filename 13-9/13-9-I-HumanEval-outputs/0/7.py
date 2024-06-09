
def change_base(x: int, base: int) -> str:
    
    digits = '0123456789ABCDEF'
    if x == 0:
        return '0'
    result = ''
    while x > 0:
        result = digits[x % base] + result
        x //= base
    return result

