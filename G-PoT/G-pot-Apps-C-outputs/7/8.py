
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

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
