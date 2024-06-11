def change_base(x: int, base: int):
    
    if x == 0:
        return '0'
    if x < 0:
        return '-' + change_base(-x, base)
    if base < 2:
        raise ValueError('base must be greater than 1')
    if base > 10:
        raise ValueError('base must be less than 10')
    if x < base:
        return str(x)
    return change_base(x // base, base) + str(x % base)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
