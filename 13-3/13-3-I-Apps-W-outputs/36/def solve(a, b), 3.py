
def solve(a, b):
    if a == b:
        return 0
    
    gcd = get_gcd(a, b)
    if gcd == 1:
        return -1
    
    return get_lcm(a, b) // gcd

def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)

def get_lcm(a, b):
    return a * b // get_gcd(a, b)

