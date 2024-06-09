
def is_consistent(n, a, b, c, d):
    return c - d <= sum(range(a - b, a + b + 1)) * n <= c + d

