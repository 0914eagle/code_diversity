def change_base(x: int, base: int):
    
    if x == 0:
        return '0'
    res = ''
    while x > 0:
        res = str(x % base) + res
        x = x // base
    return res


if __name__ == "__main__":
    import doctest
    doctest.testmod()
