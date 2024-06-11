def circular_shift(x, shift):
    
    if x < 0:
        return circular_shift(-x, shift)
    if shift < 0:
        return circular_shift(x, -shift)
    if x < 10:
        return str(x)
    if shift == 0:
        return str(x)
    if shift >= len(str(x)):
        return str(x)[::-1]
    return str(x)[shift:] + str(x)[:shift]


if