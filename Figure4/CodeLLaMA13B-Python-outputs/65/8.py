def circular_shift(x, shift):
    
    # convert to string
    x = str(x)
    # if shift is greater than length of string
    if shift > len(x):
        # return string in reverse
        return x[::-1]
    # else
    else:
        # return string with shift
        return x[shift:] + x[:shift]


if