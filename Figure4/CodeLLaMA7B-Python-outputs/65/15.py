def circular_shift(x, shift):
    
    if x < 0:
        x = -x
        sign = -1
    else:
        sign = 1
    x = sign * x
    shift = shift % 10
    if shift == 0:
        return str(x)
    else:
        return str(x % 10**shift) + str(x // 10**shift)


if __name__ == "__main__":
    import doctest
    doctest