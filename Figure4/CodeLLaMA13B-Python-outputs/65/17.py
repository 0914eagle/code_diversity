def circular_shift(x, shift):
    
    str_x = str(x)
    if shift > len(str_x):
        return str_x[::-1]
    else:
        return str_x[shift:] + str_x[:shift]


