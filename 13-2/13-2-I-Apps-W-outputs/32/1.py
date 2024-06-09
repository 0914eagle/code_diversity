
def solve(n, a, x, b, y):
    # Check if Daniel and Vlad will ever be at the same station at the same time during their journey
    if a == b or x == y:
        return "YES"
    elif a < b and x < y:
        return "NO"
    elif a > b and x > y:
        return "NO"
    else:
        return "YES"

