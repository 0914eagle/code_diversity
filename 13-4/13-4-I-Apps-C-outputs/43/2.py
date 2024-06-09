
def f1(a, b):
    # find the greatest common divisor of a and b
    gcd = find_gcd(a, b)
    # divide a and b by their gcd
    a //= gcd
    b //= gcd
    # if a and b are both 1, we only need one resistor
    if a == 1 and b == 1:
        return 1
    # if a and b are not both 1, we need at least two resistors
    return 2

def f2(a, b):
    # find the greatest common divisor of a and b
    gcd = find_gcd(a, b)
    # divide a and b by their gcd
    a //= gcd
    b //= gcd
    # if a and b are both 1, we only need one resistor
    if a == 1 and b == 1:
        return 1
    # if a and b are not both 1, we need at least two resistors
    return 2

def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(f1(a, b))

