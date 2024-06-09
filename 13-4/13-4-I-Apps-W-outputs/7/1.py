
def solve(m, x):
    # Calculate the greatest common divisor (gcd) of x and m
    gcd = get_gcd(x, m)
    
    # If gcd is 1, then x and m are coprime, and we can use the Euclidean algorithm to find the multiplicative inverse of x modulo m
    if gcd == 1:
        # Find the multiplicative inverse of x modulo m using the Extended Euclidean algorithm
        multiplicative_inverse = get_multiplicative_inverse(x, m)
        
        # Calculate the minimum number of traps needed to catch the x-mouse
        traps = (m - 1) // multiplicative_inverse + 1
        
        return traps
    
    # If gcd is not 1, then x and m are not coprime, and we cannot use the Euclidean algorithm to find the multiplicative inverse of x modulo m
    else:
        # In this case, we can simply place a trap in each room and catch the x-mouse
        traps = m
        
        return traps

def get_gcd(a, b):
    # Find the greatest common divisor (gcd) of a and b using the Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    
    return a

def get_multiplicative_inverse(a, m):
    # Find the multiplicative inverse of a modulo m using the Extended Euclidean algorithm
    b = m
    x = 0
    y = 1
    
    while a != 0:
        q = b // a
        b, a = a, b % a
        x, y = y, x - q * y
    
    return x % m

