
def create_bit_string(a, b, c, d):
    # Initialize an empty bit string
    bit_string = ""

    # Check if the given conditions are valid
    if a + b + c + d > 10**9:
        return "impossible"

    # Add 0s to the bit string to satisfy the first condition
    for i in range(a):
        bit_string += "0"

    # Add 1s to the bit string to satisfy the second condition
    for i in range(b):
        bit_string += "1"

    # Add 0s to the bit string to satisfy the third condition
    for i in range(c):
        bit_string += "0"

    # Add 1s to the bit string to satisfy the fourth condition
    for i in range(d):
        bit_string += "1"

    return bit_string

