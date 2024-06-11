


def change_base(x: int, base: int):
    
    # check if base is valid
    if base < 2 or base >= 10:
        raise ValueError("Base must be between 2 and 9")
    # convert the number to a string in the new base
    return str(int(x, base))


