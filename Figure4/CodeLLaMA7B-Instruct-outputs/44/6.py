


def change_base(x: int, base: int):
    
    # convert the number to a string in the new base
    return str(int(x, base))


# test cases
assert change_base(8, 3) == '22'
assert change_base(8, 2) == '1000'
assert change_base(7, 2) == '111'

# test cases for incorrect input
try:
    change_base(8, 10)
except ValueError:
    print("ValueError")

try:
    change_base(8, 11)
except ValueError:
    print("ValueError")

try:
    change_base(8, 12)
except ValueError:
    print("ValueError")

try:
    change_base(8, 13)
except ValueError:
    print("ValueError")

try:
    change_base(8, 14)
except ValueError:
    print("ValueError")

try:
    change_base(8, 15)
except ValueError:
    print("ValueError")
