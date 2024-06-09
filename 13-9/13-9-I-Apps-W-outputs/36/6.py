
import math

def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solve(n, x, arr):
    numerator = 0
    denominator = 0
    for i in range(n):
        numerator += 1 / (x ** arr[i])
        denominator += arr[i]
    gcd = get_gcd(numerator, denominator)
    return numerator // gcd % 1000000007

