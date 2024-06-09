
def get_minimum_traps(m, x):
    # Calculate the greatest common divisor (gcd) of x and m
    gcd = get_gcd(x, m)
    
    # If gcd is 1, then x and m are relatively prime
    if gcd == 1:
        # In this case, the minimum number of traps is m
        return m
    else:
        # If gcd is not 1, then x and m have a common factor greater than 1
        # In this case, the minimum number of traps is m // gcd
        return m // gcd

def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

m = int(input())
x = int(input())
print(get_minimum_traps(m, x))

