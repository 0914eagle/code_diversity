
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solve(n, x, arr):
    numerator = 0
    denominator = 0
    for i in arr:
        numerator += x**i
        denominator += i
    gcd_val = gcd(numerator, denominator)
    return numerator // gcd_val % 1000000007

