
def solve(n, divisors):
    # Sort the divisors in ascending order
    divisors.sort()

    # Initialize the minimum possible value of x as the smallest divisor
    x = divisors[0]

    # Iterate through the divisors and find the smallest value of x that is greater than or equal to the divisor
    for divisor in divisors:
        while x < divisor:
            x += 1

        # If the current value of x is not a divisor, it is not possible to find such number
        if x % divisor != 0:
            return -1

    # If all divisors are valid, return the minimum possible value of x
    return x

