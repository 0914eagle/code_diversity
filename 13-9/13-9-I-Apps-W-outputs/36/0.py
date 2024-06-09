
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solve(n, x, arr):
    numerator = 0
    denominator = 0
    for i in arr:
        numerator += 1 / x**i
        denominator += x**i
    fraction = numerator / denominator
    s = fraction.numerator
    t = fraction.denominator
    gcd_st = gcd(s, t)
    return gcd_st % (10**9 + 7)

