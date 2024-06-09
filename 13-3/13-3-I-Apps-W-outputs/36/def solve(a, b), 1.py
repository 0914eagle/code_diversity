
def solve(a, b):
    # Find the greatest common divisor of a and b
    gcd = find_gcd(a, b)
    
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
            a //= gcd
            b //= gcd
        count += 1
    
    return count

def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

