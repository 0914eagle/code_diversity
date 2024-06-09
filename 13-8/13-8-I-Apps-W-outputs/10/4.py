
def solve(n, k, A, B):
    # Calculate the greatest common divisor (gcd) of n and k
    gcd = _gcd(n, k)
    # If the gcd is 1, then n is not divisible by k, so we can't divide x by k
    if gcd == 1:
        return -1
    # Otherwise, divide x by the gcd to get the minimum number of divisions needed
    divisions = n // gcd
    # Calculate the total cost of the divisions
    cost = divisions * B
    # Add the cost of subtracting 1 from x the number of times needed to get to 1
    cost += abs(n - 1) * A
    return cost

def _gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

