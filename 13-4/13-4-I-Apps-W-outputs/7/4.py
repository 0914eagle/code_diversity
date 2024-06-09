
def get_min_traps(m, x):
    # Calculate the greatest common divisor (gcd) of x and m
    gcd = get_gcd(x, m)
    
    # If gcd is 1, then x and m are coprime, and we can use the Euclidean algorithm to find the multiplicative inverse of x modulo m
    if gcd == 1:
        # Find the multiplicative inverse of x modulo m using the Extended Euclidean algorithm
        inv = get_multiplicative_inverse(x, m)
        
        # Calculate the minimum number of traps needed to catch the x-mouse
        traps = (m - 1) // gcd
        
        # If the multiplicative inverse of x modulo m exists, then we can catch the x-mouse by placing traps in rooms x, 2x, 3x, ..., (m-1)x modulo m
        if inv != -1:
            return traps
    
    # If gcd is not 1, then x and m are not coprime, and we cannot use the Euclidean algorithm to find the multiplicative inverse of x modulo m
    # In this case, we can catch the x-mouse by placing traps in rooms 0, 1, 2, ..., m-1
    return m

def get_gcd(a, b):
    # Base case: if b is 0, the gcd is a
    if b == 0:
        return a
    
    # Recursive case: calculate the gcd of b and the remainder of a divided by b
    return get_gcd(b, a % b)

def get_multiplicative_inverse(a, m):
    # Calculate the extended Euclidean algorithm of a and m
    g, x, y = egcd(a, m)
    
    # If the gcd is 1, then x is the multiplicative inverse of a modulo m
    if g == 1:
        return x % m
    
    # If the gcd is not 1, then there is no multiplicative inverse
    return -1

def egcd(a, b):
    # Base case: if b is 0, the gcd is a, and the multiplicative inverse is 0
    if b == 0:
        return a, 0, 1
    
    # Recursive case: calculate the extended Euclidean algorithm of b and the remainder of a divided by b
    g, y, x = egcd(b, a % b)
    return g, x, y - (a // b) * x

