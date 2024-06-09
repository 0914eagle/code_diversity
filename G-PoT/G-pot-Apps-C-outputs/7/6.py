
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a, b = map(int, input().split())
resistors_needed = b // gcd(a, b)
print(resistors_needed)
