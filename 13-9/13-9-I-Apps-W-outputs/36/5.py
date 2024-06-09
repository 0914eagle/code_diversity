
def solve(n, x, arr):
    # Calculate the denominator
    denominator = 1
    for i in arr:
        denominator *= x ** i
    
    # Calculate the numerator
    numerator = 0
    for i in arr:
        numerator += x ** -i
    
    # Calculate the greatest common divisor
    gcd = gcd_euclid(numerator, denominator)
    
    # Return the result modulo 1000000007
    return gcd % 1000000007

def gcd_euclid(a, b):
    if b == 0:
        return a
    else:
        return gcd_euclid(b, a % b)

