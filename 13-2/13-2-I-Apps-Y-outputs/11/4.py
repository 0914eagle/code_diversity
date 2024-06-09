
def solve(a, b):
    # Find the smallest common multiple of a and b
    scm = a * b // gcd(a, b)
    return scm

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

