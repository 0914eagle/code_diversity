
def solve(n, divisors):
    # Sort the divisors in ascending order
    divisors.sort()

    # Initialize the minimum possible value of x as the smallest divisor
    x = divisors[0]

    # Iterate through the divisors and check if they are almost all divisors of x
    for i in range(1, n):
        if divisors[i] != x * (i + 1):
            return -1

    return x

