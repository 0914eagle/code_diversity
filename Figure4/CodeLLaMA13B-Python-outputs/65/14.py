def circular_shift(x, shift):
    
    # x_str = str(x)
    # if len(x_str) <= shift:
    #     return x_str[::-1]
    # return x_str[shift:] + x_str[:shift]
    return str(x)[shift:] + str(x)[:shift]


if