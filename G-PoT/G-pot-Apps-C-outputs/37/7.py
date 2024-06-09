
import math

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def find_smallest_distance(m, x, y):
    n = len(m)
    M = 1
    for i in range(n):
        M *= m[i]
    
    z = 0
    for i in range(n):
        Mi = M // m[i]
        gcd, t, _ = gcd_extended(Mi, m[i])
        z += x[i] * Mi * t
    
    z = z % M
    for i in range(n):
        if z % m[i] < x[i] - y[i]:
            z += math.ceil((x[i] - y[i] - z % m[i]) / m[i]) * m[i]
    
    return z

m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(find_smallest_distance(m, x, y))
