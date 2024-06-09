
def solve(a, b, c, d):
    # Initialize the bit string to an empty string
    bit_string = ""

    # While there are still elements to add to the bit string
    while a + b + c + d > 0:
        # If the number of 0s is greater than or equal to the number of 1s
        if a >= b:
            # Add a 0 to the bit string
            bit_string += "0"
            # Decrement the number of 0s
            a -= 1
        # Otherwise, if the number of 1s is greater than or equal to the number of 0s
        elif b >= a:
            # Add a 1 to the bit string
            bit_string += "1"
            # Decrement the number of 1s
            b -= 1
        # Otherwise, if the number of 0s is greater than or equal to the number of 1s
        elif c >= d:
            # Add a 0 to the bit string
            bit_string += "0"
            # Decrement the number of 0s
            c -= 1
        # Otherwise, if the number of 1s is greater than or equal to the number of 0s
        else:
            # Add a 1 to the bit string
            bit_string += "1"
            # Decrement the number of 1s
            d -= 1

    # Return the bit string
    return bit_string

