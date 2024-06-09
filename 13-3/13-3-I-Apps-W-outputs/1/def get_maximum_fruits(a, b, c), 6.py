
def get_maximum_fruits(a, b, c):
    # Find the greatest common divisor of a, b, and c
    gcd = find_gcd(a, b, c)
    # Divide a, b, and c by their GCD
    a //= gcd
    b //= gcd
    c //= gcd
    # Find the least common multiple of a, b, and c
    lcm = find_lcm(a, b, c)
    # Return the least common multiple divided by the greatest common divisor
    return lcm // gcd

def find_gcd(a, b, c):
    if a == 0:
        return b
    if b == 0:
        return a
    if c == 0:
        return a
    while True:
        if a % b == 0 and b % c == 0:
            return a
        a, b = b, a % b
        b, c = c, b % c
        a, b = b, a % b
        b, c = c, b % c

def find_lcm(a, b, c):
    return a * b // find_gcd(a, b)

