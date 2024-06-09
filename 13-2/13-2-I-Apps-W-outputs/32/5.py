
def solve(n, a, x, b, y):
    # Check if Daniel and Vlad will ever be at the same station at the same time during their journey
    if a == x or b == y:
        return "NO"
    if a < x and b < y:
        return "NO"
    if a > x and b > y:
        return "NO"
    return "YES"

