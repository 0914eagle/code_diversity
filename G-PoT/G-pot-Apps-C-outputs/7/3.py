
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
resistors = 0

while a != 1:
    resistors += a // b
    a, b = b, a % b

print(resistors + b)
