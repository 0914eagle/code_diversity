
import math

def solve(n, x, arr):
    numerator = 0
    denominator = 0
    for i in arr:
        numerator += x ** i
        denominator += i
    gcd = math.gcd(numerator, denominator)
    return gcd % 1000000007

