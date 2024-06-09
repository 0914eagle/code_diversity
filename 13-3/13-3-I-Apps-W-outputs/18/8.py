
from math import gcd

def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def solve(A, B, n, x):
    result = x
    for i in range(n):
        result = (A * result + B) % 1000000007
    return result

A, B, n, x = map(int, input().split())
print(solve(A, B, n, x))

