
def can_switch_garlands(k1, k2, k3):
    # Check if k1, k2, and k3 are positive
    if k1 <= 0 or k2 <= 0 or k3 <= 0:
        return "NO"

    # Check if the greatest common divisor of k1, k2, and k3 is 1
    if __gcd(k1, k2) != 1 or __gcd(k1, k3) != 1 or __gcd(k2, k3) != 1:
        return "NO"

    # Check if the sum of k1, k2, and k3 is less than or equal to 1500
    if k1 + k2 + k3 > 1500:
        return "NO"

    return "YES"

