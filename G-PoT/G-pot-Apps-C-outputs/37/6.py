
import math

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def chinese_remainder_theorem(n, a):
    sum = 0
    prod = math.prod(n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        _, inv, _ = gcd_extended(p, n_i)
        sum += a_i * inv * p
    return sum % prod

m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

n = m
a = [(x[i] - y[i]) % m[i] for i in range(3)]

z = chinese_remainder_theorem(n, a)
print(z)
