
from sys import stdin, stdout
from math import gcd

def mod_pow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

def extended_euclidean(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_euclidean(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(a, m):
    g, x, y = extended_euclidean(a, m)
    if g != 1:
        raise ValueError
    return x % m

def mod_mul_inverse(a, m):
    return mod_pow(a, m - 2, m)

def mod_div(a, b, m):
    return mod_mul(a, mod_inverse(b, m), m)

def mod_add(a, b, m):
    return (a + b) % m

def mod_sub(a, b, m):
    return (a - b) % m

def mod_mul(a, b, m):
    return (a * b) % m

def solve(A, B, n, x):
    result = 0
    for i in range(n):
        result = mod_add(result, mod_mul(A, x, 1000000007), 1000000007)
        x = mod_add(x, B, 1000000007)
    return result % 1000000007

A, B, n, x = map(int, stdin.readline().split())
print(solve(A, B, n, x))

