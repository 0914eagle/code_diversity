
def solve(n, a, b, c, d):
    if c - d <= n * (a - b) <= c + d:
        return "Yes"
    else:
        return "No"

