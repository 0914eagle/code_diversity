
def solve(n, divisors):
    # Sort the divisors in ascending order
    divisors.sort()

    # Initialize the minimum possible value of x as the smallest divisor
    x = divisors[0]

    # Iterate through the divisors and check if they are valid
    for i in range(1, n):
        # Check if the current divisor is equal to the previous divisor multiplied by 2
        if divisors[i] != divisors[i-1] * 2:
            # If it is not, then the input data is contradictory and it is impossible to find such number
            return -1

    # If all divisors are valid, return the minimum possible value of x
    return x

