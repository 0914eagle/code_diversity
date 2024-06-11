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
    x_str = str(x)
    if shift >= len(x_str):
        return sign + x_str[::-1]
    return sign + x_str[shift:] + x_str[:shift]


if