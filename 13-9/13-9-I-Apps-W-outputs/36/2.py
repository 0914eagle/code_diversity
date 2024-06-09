
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve(n, x, arr):
    numerator = 0
    denominator = 0
    for a in arr:
        numerator += x ** a
        denominator += a
    gcd_value = gcd(numerator, denominator)
    return numerator // gcd_value % 1000000007

