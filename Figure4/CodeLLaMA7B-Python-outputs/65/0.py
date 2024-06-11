def circular_shift(x, shift):
    
    if shift < 0:
        shift = shift * -1
        x = int(str(x)[::-1])
    return str(x)[shift:] + str(x)[:shift]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
