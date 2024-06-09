
def solve(a, b):
    # Find the greatest common divisor of a and b
    gcd = _gcd(a, b)
    
    # If the gcd is 1, it means that a and b are coprime and it is impossible to make them equal
    if gcd == 1:
        return -1
    
    # If the gcd is not 1, find the minimum number of operations needed to make the pieces equal
    count = 0
    while a != b:
        if a % gcd == 0:
            a //= gcd
        elif b % gcd == 0:
            b //= gcd
        else:
            a, b = b, a
        count += 1
    return count

def _gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

