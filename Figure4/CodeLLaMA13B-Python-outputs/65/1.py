def circular_shift(x, shift):
    
    "*** YOUR CODE HERE ***"
    x = str(x)
    if shift > len(x):
        return x[::-1]
    else:
        return x[shift:] + x[:shift]


