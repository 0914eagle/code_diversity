
def restore_numbers(divisors):
    # Sort the divisors in ascending order
    divisors.sort()

    # Initialize x and y to 1
    x = 1
    y = 1

    # Iterate through the divisors
    for divisor in divisors:
        # If the divisor is not a multiple of x, set x to the next multiple of x that is greater than or equal to the divisor
        if divisor % x != 0:
            x = x * (divisor // x + 1)

        # If the divisor is not a multiple of y, set y to the next multiple of y that is greater than or equal to the divisor
        if divisor % y != 0:
            y = y * (divisor // y + 1)

    # Return the values of x and y
    return x, y

