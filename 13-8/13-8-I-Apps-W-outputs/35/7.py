
def is_valid_package(n, a, b, c, d):
    return c - d <= sum(range(a - b, a + b + 1)) <= c + d

