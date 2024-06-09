
def create_bit_string(a, b, c, d):
    # Initialize a list to store the bit string
    bit_string = []

    # Check if the given conditions are valid
    if a + b + c + d > 10**9:
        return "impossible"

    # Add 0s to the bit string to satisfy condition 1
    for i in range(a):
        bit_string.append(0)

    # Add 1s to the bit string to satisfy condition 2
    for i in range(b):
        bit_string.append(1)

    # Add 0s to the bit string to satisfy condition 3
    for i in range(c):
        bit_string.append(0)

    # Add 1s to the bit string to satisfy condition 4
    for i in range(d):
        bit_string.append(1)

    # Return the bit string
    return "".join(str(x) for x in bit_string)

