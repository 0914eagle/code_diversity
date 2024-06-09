
from sys import stdin, stdout
from math import gcd

def extended_euclid(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, gcd = extended_euclid(b, a % b)
        return y, x - (a // b) * y, gcd

def modular_inverse(a, m):
    x, y, gcd = extended_euclid(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

def modular_exponentiation(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def solve(A, B, n, x):
    modulus = 1000000007
    gcd, x, y = extended_euclid(A, modulus)
    if gcd != 1:
        return -1
    else:
        return (modular_exponentiation(A, n, modulus) * x + modular_exponentiation(B, n, modulus) * y) % modulus

t = int(input())
for _ in range(t):
    A, B, n, x = map(int, input().split())
    print(solve(A, B, n, x))

