def circular_shift(x, shift):
    
    if shift > len(str(x)):
        return str(x)[::-1]
    else:
        return str(x) + str(x)[shift:]


