
x, y = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

gcd_xy = gcd(x, y)
result = x // gcd_xy - 1

print(result)
