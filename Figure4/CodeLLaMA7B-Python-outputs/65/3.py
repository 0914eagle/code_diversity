def circular_shift(x, shift):
    
    if shift == 0:
        return str(x)
    if x == 0:
        return '0'
    if x < 0:
        x = -x
        sign = '-'
    else:
        sign = ''
    x = str(x)
    if len(x) < shift:
        return x[::-1]
    return sign + x[shift:] + x[:shift]


