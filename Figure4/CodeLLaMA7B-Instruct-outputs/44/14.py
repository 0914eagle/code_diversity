


def change_base(x: int, base: int):
    
    # convert the number to a string in the new base
    return str(int(x, base))


# test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'


