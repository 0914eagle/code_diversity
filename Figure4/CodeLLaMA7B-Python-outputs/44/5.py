def change_base(x: int, base: int):
    
    if x == 0:
        return '0'
    res = ''
    while x:
        res = str(x % base) + res
        x //= base
    return res


if __name__ ==