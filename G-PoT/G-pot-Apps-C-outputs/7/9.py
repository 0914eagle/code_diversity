
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
resistors = 0

while a != 1 or b != 1:
    if a > b:
        resistors += a // b
        a %= b
    else:
        resistors += b // a
        b %= a

print(resistors)
