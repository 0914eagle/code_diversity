
def solve(a, b):
    # Find the greatest common divisor of a and b
    gcd = _gcd(a, b)
    
    # If the gcd is 1, it means that a and b are coprime and it is impossible to make them equal
    if gcd == 1:
        return -1
    
    # Otherwise, find the minimum number of operations needed to make a and b equal
    # by dividing them by the gcd
    return a // gcd + b // gcd

def _gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

