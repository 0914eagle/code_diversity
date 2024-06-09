
def solve(a, b):
    # Find the greatest common divisor of a and b
    gcd = find_gcd(a, b)
    
    # If the gcd is 1, it means that a and b are already co-prime
    # and it is not possible to make them equal
    if gcd == 1:
        return -1
    
    # Otherwise, find the minimum number of operations needed to make them equal
    return (a // gcd) + (b // gcd)

def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

