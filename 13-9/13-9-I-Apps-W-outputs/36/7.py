
def solve(n, x, a):
    # Calculate the sum of the fractions
    sum_fractions = 0
    for i in range(n):
        sum_fractions += 1 / (x ** a[i])

    # Calculate the denominator
    denominator = 0
    for i in range(n):
        denominator += a[i]

    # Calculate the greatest common divisor of the numerator and denominator
    gcd = gcd_euclid(sum_fractions, denominator)

    # Return the result modulo 1000000007
    return gcd % 1000000007

def gcd_euclid(a, b):
    if b == 0:
        return a
    else:
        return gcd_euclid(b, a % b)

