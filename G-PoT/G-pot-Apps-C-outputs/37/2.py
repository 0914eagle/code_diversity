
import math

def chinese_remainder_theorem(n, a):
    sum = 0
    prod = math.prod(n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * pow(p, -1, n_i) * p
    return sum % prod

m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

n = m
a = [(x[i] - y[i]) % m[i] for i in range(3)]

z = chinese_remainder_theorem(n, a)
print(z)
