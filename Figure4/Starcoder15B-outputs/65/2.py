def circular_shift(x, shift):
    
    if shift == 0:
        return str(x)
    s = str(x)
    shift = shift % len(s)
    return s[shift:] + s[:shift]

