
def convert_to_celsius(fahrenheit):
    a, b = fahrenheit.split("/")
    a, b = int(a), int(b)
    c = (9 * a + 32 * b) // (5 * b)
    d = b
    g = gcd(c, d)
    return f"{c//g}/{d//g}"

