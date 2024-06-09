
def get_min_traps(m, x):
    # Calculate the greatest common divisor (gcd) of x and m
    gcd = get_gcd(x, m)
    
    # If gcd is 1, then x and m are coprime
    if gcd == 1:
        # In this case, the minimum number of traps is m
        return m
    else:
        # If gcd is not 1, then x and m are not coprime
        # In this case, the minimum number of traps is gcd
        return gcd

def get_gcd(a, b):
    # Base case: if b is 0, the gcd is a
    if b == 0:
        return a
    
    # Recursive case: calculate the gcd of b and the remainder of a divided by b
    else:
        return get_gcd(b, a % b)

m = int(input())
x = int(input())
print(get_min_traps(m, x))

