
def can_switch_on_garlands(k1, k2, k3):
    # Check if k1, k2, and k3 are positive
    if k1 <= 0 or k2 <= 0 or k3 <= 0:
        return "NO"

    # Check if the greatest common divisor of k1, k2, and k3 is 1
    if __gcd(k1, k2) != 1 or __gcd(k1, k3) != 1 or __gcd(k2, k3) != 1:
        return "NO"

    # Check if the sum of k1, k2, and k3 is even
    if k1 + k2 + k3 % 2 == 0:
        return "NO"

    # Check if the product of k1, k2, and k3 is odd
    if k1 * k2 * k3 % 2 == 0:
        return "NO"

    return "YES"

