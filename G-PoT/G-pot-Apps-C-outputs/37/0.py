
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
    
    z = 0
    for i in range(n):
        z += x[i] * M_i[i] * M_i_inv[i]
    
    z %= M
    for i in range(n):
        if z % m[i] > x[i]:
            z -= z % m[i] - x[i]
        elif z % m[i] < x[i]:
            z += x[i] - z % m[i]
    
    return z

m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(find_smallest_distance(m, x, y))
