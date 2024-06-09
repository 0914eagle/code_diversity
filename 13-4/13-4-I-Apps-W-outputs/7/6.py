
def get_min_traps(m, x):
    # Calculate the greatest common divisor (gcd) of x and m
    gcd = get_gcd(x, m)
    
    # If gcd is 1, then x and m are coprime, and we can use the Euclidean algorithm to find the multiplicative inverse of x modulo m
    if gcd == 1:
        # Find the multiplicative inverse of x modulo m using the Extended Euclidean algorithm
        multiplicative_inverse = get_multiplicative_inverse(x, m)
        
        # Calculate the minimum number of traps needed to catch the x-mouse
        min_traps = (m - 1) // multiplicative_inverse
        
        return min_traps
    
    # If gcd is not 1, then x and m are not coprime, and we cannot use the Euclidean algorithm to find the multiplicative inverse of x modulo m
    else:
        # Return the maximum number of traps needed to catch the x-mouse
        return m

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
    
    # The multiplicative inverse of a modulo m is x
    return x % m

def egcd(a, b):
    # Base case: if b is 0, the gcd is a, and the multiplicative inverse is 1
    if b == 0:
        return a, 1, 0
    
    # Recursive case: calculate the gcd of b and the remainder of a divided by b, and the multiplicative inverse of a modulo b
    g, y, x = egcd(b, a % b)
    return g, x, y - (a // b) * x

