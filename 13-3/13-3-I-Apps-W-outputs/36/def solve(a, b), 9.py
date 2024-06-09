
def solve(a, b):
    # Find the greatest common divisor of a and b
    gcd = _gcd(a, b)
    
    # If the pieces are already equal, return 0
    if a == b:
        return 0
    
    # If the fox is lying and it is impossible to make the pieces equal, return -1
    if gcd == 1:
        return -1
    
    # Initialize the minimum number of operations to 0
    min_ops = 0
    
    # While a and b are not equal
    while a != b:
        # If a is divisible by gcd, eat a/gcd of a
        if a % gcd == 0:
            a -= a // gcd
            min_ops += 1
        # If b is divisible by gcd, eat b/gcd of b
        if b % gcd == 0:
            b -= b // gcd
            min_ops += 1
    
    # Return the minimum number of operations
    return min_ops

def _gcd(a, b):
    if b == 0:
        return a
    else:
        return _gcd(b, a % b)

