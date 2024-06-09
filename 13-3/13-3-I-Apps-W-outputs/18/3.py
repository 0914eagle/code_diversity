
from sys import stdin, stdout
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

def extended_euclidean(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_euclidean(b % a, a)
        return (g, x - (b // a) * y, y)

def modular_inverse(a, m):
    g, x, y = extended_euclidean(a, m)
    if g != 1:
        return None
    return x % m

def modular_multiplicative_inverse(n, modulus):
    return modular_inverse(n, modulus)

def modular_additive_inverse(n, modulus):
    return (-n) % modulus

def modular_subtractive_inverse(n, modulus):
    return modular_additive_inverse(-n, modulus)

def modular_division(dividend, divisor, modulus):
    return (dividend * modular_multiplicative_inverse(divisor, modulus)) % modulus

def modular_fraction(numerator, denominator, modulus):
    return (numerator * modular_multiplicative_inverse(denominator, modulus)) % modulus

def solve(a, b, n, x):
    result = 0
    for i in range(n):
        result = (result + modular_fraction(a, b, 1000000007)) % 1000000007
    return result

def main():
    a, b, n, x = map(int, stdin.readline().strip().split())
    stdout.write(str(solve(a, b, n, x)))

if __name__ == '__main__':
    main()

