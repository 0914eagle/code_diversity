
def solve(a, b):
    # Find the greatest common divisor of a and b
    gcd = find_gcd(a, b)
    
    # If the gcd is 1, it means that a and b are already co-prime
    # and it is impossible to make them equal
    if gcd == 1:
        return -1
    
    # If the gcd is not 1, we can make the pieces equal by
    # eating a little bit of each piece until they are equal
    count = 0
    while a != b:
        if a > b:
            a -= gcd
        else:
            b -= gcd
        count += 1
    
    return count

def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

