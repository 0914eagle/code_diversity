def change_base(x: int, base: int):
    
    if x == 0:
        return '0'
    if x < 0:
        return '-' + change_base(-x, base)
    else:
        return change_base(x // base, base) + str(x % base)


if __name__ == '__main__':
    import doctest
    doctest.testmod()