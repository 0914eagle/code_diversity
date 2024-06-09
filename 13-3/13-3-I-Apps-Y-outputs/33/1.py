
def solve(divisors):
    # Sort the divisors in ascending order
    divisors.sort()

    # Initialize the minimum possible value of x as 1
    x = 1

    # Iterate through the divisors
    for d in divisors:
        # If the current divisor is not a multiple of the previous divisor,
        # it means that the previous divisor is not the last divisor of x,
        # so we can update the minimum possible value of x
        if d % x != 0:
            x *= d

    # Return the minimum possible value of x
    return x

