
def solve(n, a, b, c, d):
    return "Yes" if c - d <= a * n <= c + d and b * n >= a * n >= a - b * n else "No"

