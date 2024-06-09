
def solve(n, divisors):
    # Sort the divisors in ascending order
    divisors.sort()

    # Initialize the minimum possible value of x as the smallest divisor
    x = divisors[0]

    # Iterate through the divisors and check if they are valid
    for i in range(1, n):
        # Check if the current divisor is a multiple of the previous divisor
        if divisors[i] % divisors[i-1] != 0:
            # If it is not a multiple, the input data is contradictory
            return -1

        # Update the minimum possible value of x
        x *= divisors[i-1]

    # Return the minimum possible value of x
    return x

