
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def min_resistors(a, b):
    if a == b:
        return 1
    if a < b:
        a, b = b, a
    return b + min_resistors(a - b, b)

a, b = map(int, input().split())
common_divisor = gcd(a, b)
a //= common_divisor
b //= common_divisor
print(min_resistors(a, b))
