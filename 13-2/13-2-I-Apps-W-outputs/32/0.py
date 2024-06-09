
def solve(n, a, x, b, y):
    # Check if Daniel and Vlad will ever be at the same station at the same time during their journey
    if a == b or a == y or x == b or x == y:
        return "YES"
    else:
        return "NO"

