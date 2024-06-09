
import math

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - (a // b) * y

def find_smallest_distance(m, x, y):
    n = len(m)
    M = math.prod(m)
    M_i = [M // mi for mi in m]
    M_i_inv = [extended_gcd(Mi, mi)[1] for Mi, mi in zip(M_i, m)]
    z = sum((x[i] * M_i[i] * M_i_inv[i]) % M for i in range(n))
    return z % M

m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(find_smallest_distance(m, x, y))
