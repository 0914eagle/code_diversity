
def convert_to_celsius(fahrenheit):
    a, b = fahrenheit.split('/')
    a, b = int(a), int(b)
    c = (9 * a + 32 * b) // (5 * b)
    d = b
    g = gcd(c, d)
    return f"{c//g}/{d//g}"

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

fahrenheit = input()
print(convert_to_celsius(fahrenheit))

