
def solve(k1, k2, k3):
    # Check if k1, k2, and k3 are pairwise coprime
    if __gcd(k1, k2) != 1 or __gcd(k1, k3) != 1 or __gcd(k2, k3) != 1:
        return "NO"
    
    # Check if k1, k2, and k3 are all less than or equal to 1500
    if k1 > 1500 or k2 > 1500 or k3 > 1500:
        return "NO"
    
    # Check if the sum of k1, k2, and k3 is less than or equal to 1500
    if k1 + k2 + k3 > 1500:
        return "NO"
    
    return "YES"

