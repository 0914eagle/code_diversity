


def change_base(x: int, base: int):
    
    # convert the number to a string in the new base
    return str(int(x, base))


# test cases
assert change_base(8, 3) == '22'
assert change_base(8, 2) == '1000'
assert change_base(7, 2) == '111'

# additional tests
assert change_base(0, 2) == '0'
assert change
