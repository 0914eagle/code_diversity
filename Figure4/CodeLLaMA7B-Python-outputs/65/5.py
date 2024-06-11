def circular_shift(x, shift):
    
    # BEGIN PROBLEM 1
    if shift > len(str(x)):
        return str(x)[::-1]
    else:
        return str(x)[shift:] + str(x)[:shift]
    # END PROBLEM 1


