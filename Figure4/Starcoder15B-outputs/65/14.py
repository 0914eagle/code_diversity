def circular_shift(x, shift):
    
    if shift == 0:
        return str(x)
    else:
        digits = str(x)
        shift = shift % len(digits)
        return digits[shift:] + digits[:shift]


