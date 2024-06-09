
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
resistors_needed = b // gcd(a, b)
print(resistors_needed)
