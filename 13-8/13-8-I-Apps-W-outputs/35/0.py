
def solve(n, a, b, c, d):
    if c - d < n * (a - b) or c + d < n * (a + b):
        return "No"
    return "Yes"

