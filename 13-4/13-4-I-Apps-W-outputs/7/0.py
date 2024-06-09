
def get_min_traps(m, x):
    # Calculate the greatest common divisor (gcd) of x and m
    gcd = get_gcd(x, m)
    
    # If gcd is 1, then x and m are coprime, and we can use the Euclidean algorithm to find the multiplicative inverse of x modulo m
    if gcd == 1:
        # Find the multiplicative inverse of x modulo m using the Extended Euclidean algorithm
        inv = get_multiplicative_inverse(x, m)
        
        # If the multiplicative inverse exists, we can use it to find the minimum number of traps needed to catch the x-mouse
        if inv != -1:
            return inv
    
    # If gcd is not 1 or the multiplicative inverse does not exist, we cannot catch the x-mouse
    return -1

def get_gcd(a, b):
    # Base case: if b is 0, the gcd is a
    if b == 0:
        return a
    
    # Recursive case: calculate the gcd of b and the remainder of a divided by b
    else:
        return get_gcd(b, a % b)

def get_multiplicative_inverse(a, m):
    # Calculate the extended Euclidean algorithm of a and m
    g, x, y = egcd(a, m)
    
    # If g is 1, then x is the multiplicative inverse of a modulo m
    if g == 1:
        return x % m
    
    # If g is not 1, then the multiplicative inverse does not exist
    else:
        return -1

def egcd(a, b):
    # Base case: if b is 0, the gcd is a and the multiplicative inverse is 1
    if b == 0:
        return a, 1, 0
    
    # Recursive case: calculate the extended Euclidean algorithm of b and the remainder of a divided by b
    g, y, x = egcd(b, a % b)
    return g, x, y - (a // b) * x

