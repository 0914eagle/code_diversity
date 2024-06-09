
import math

def find_smallest_distance(m1, m2, m3, x1, x2, x3, y1, y2, y3):
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        else:
            d, x, y = extended_gcd(b, a % b)
            return d, y, x - (a // b) * y

    def chinese_remainder_theorem(a, m):
        M = math.prod(m)
        result = 0
        for ai, mi in zip(a, m):
            Mi = M // mi
            _, ti, _ = extended_gcd(mi, Mi)
            result += ai * Mi * ti
        return result % M

    z = chinese_remainder_theorem([x1, x2, x3], [m1, m2, m3])
    return z

# Input
m1, m2, m3 = map(int, input().split())
x1, x2, x3 = map(int, input().split())
y1, y2, y3 = map(int, input().split())

# Output
print(find_smallest_distance(m1, m2, m3, x1, x2, x3, y1, y2, y3))
