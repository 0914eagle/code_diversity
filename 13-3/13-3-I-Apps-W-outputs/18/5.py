
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

t = int(stdin.readline().strip())
for _ in range(t):
    a, b, n, x = map(int, stdin.readline().strip().split())
    g = x
    for i in range(n):
        g = (a * g + b) % 1000000007
    stdout.write(str(g) + '\n')

