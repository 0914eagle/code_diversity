
import math

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - (a // b) * y

def chinese_remainder_theorem(n, a):
    sum = 0
    prod = math.prod(n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        _, s, _ = extended_gcd(n_i, p)
        sum += a_i * s * p
    return sum % prod

m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

n = m
a = [(x[i] - y[i]) % m[i] for i in range(3)]

z = chinese_remainder_theorem(n, a)
print(z)
