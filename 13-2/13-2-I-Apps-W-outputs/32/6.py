
def solve(n, a, x, b, y):
    # Check if Daniel and Vlad will ever be at the same station at the same time during their journey
    if a == x or b == y:
        return "YES"
    elif a == b or x == y:
        return "NO"
    else:
        # Check if Daniel and Vlad will ever be at the same station at the same time during their journey
        if (a < b and x < y) or (a > b and x > y):
            return "NO"
        else:
            return "YES"

