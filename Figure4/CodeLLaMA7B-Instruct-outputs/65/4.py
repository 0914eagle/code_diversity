

def circular_shift(x, shift):
    
    num_digits = len(str(x))
    if shift > num_digits:
        return str(x)[::-1]
    else:
        return str(x)[shift:] + str(x)[:shift]


