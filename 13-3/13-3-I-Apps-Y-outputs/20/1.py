
def restore_numbers(divisors):
    # Sort the divisors in ascending order
    divisors.sort()

    # Initialize x and y to 1
    x = 1
    y = 1

    # Iterate through the divisors
    for divisor in divisors:
        # If the divisor is not a multiple of x, multiply x by the divisor
        if divisor % x == 0:
            x *= divisor
        # If the divisor is not a multiple of y, multiply y by the divisor
        elif divisor % y == 0:
            y *= divisor
        # If the divisor is not a multiple of both x and y, set y to the product of x and the divisor
        else:
            y = x * divisor

    # Return the values of x and y
    return x, y

