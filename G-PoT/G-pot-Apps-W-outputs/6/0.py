
x, y = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

gcd_xy = gcd(x, y)
result = (x + y - gcd_xy*2) // gcd_xy
print(result)
