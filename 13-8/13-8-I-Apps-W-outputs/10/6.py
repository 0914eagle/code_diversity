
def solve(n, k, A, B):
    # Calculate the greatest common divisor (gcd) of n and k
    gcd = _gcd(n, k)
    # If the gcd is 1, there is no need to divide n by k
    if gcd == 1:
        # Return the number of operations to make n equal to 1
        return n * A
    # Calculate the number of divisions needed to make n equal to the gcd
    divisions = 0
    while n % gcd == 0:
        n //= gcd
        divisions += 1
    # Return the total cost of the operations
    return divisions * B + n * A

def _gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

