
def solve(divisors):
    # Sort the divisors in ascending order
    divisors.sort()

    # Initialize the minimum possible value of x as the smallest divisor
    x = divisors[0]

    # Iterate through the divisors and check if they are valid
    for i in range(1, len(divisors)):
        if divisors[i] != x * (i + 1):
            return -1

    # If all divisors are valid, return the minimum possible value of x
    return x

