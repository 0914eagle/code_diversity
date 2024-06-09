
def solve(a, b):
    # Find the greatest common divisor of a and b
    gcd = find_gcd(a, b)
    
    # If the gcd is 1, it means that a and b are already co-prime
    # and it is impossible to make them equal
    if gcd == 1:
        return -1
    
    # If the gcd is not 1, we can make the pieces equal by eating
    # a multiple of the gcd. The minimum number of operations is the
    # number of times we need to eat the gcd to make the pieces equal.
    return b // gcd

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

