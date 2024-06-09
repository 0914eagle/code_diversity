
def solve(a, b):
    if a == b:
        return 0
    
    gcd = find_gcd(a, b)
    if gcd == 1:
        return -1
    
    return b // gcd

def find_gcd(a, b):
    if b == 0:
        return a
    return find_gcd(b, a % b)

