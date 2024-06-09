
def solve(k1, k2, k3):
    # Check if k1, k2, and k3 are coprime
    if __gcd(k1, k2) == 1 and __gcd(k1, k3) == 1 and __gcd(k2, k3) == 1:
        return "YES"
    else:
        return "NO"

