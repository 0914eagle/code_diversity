
def circular_shift(x: int, shift: int) -> str:
    
    x_str = str(x)
    num_digits = len(x_str)
    if shift > num_digits:
        return x_str[::-1]
    else:
        return x_str[shift:] + x_str[:shift]

