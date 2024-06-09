
def solve(n, k, m, a):
    total = sum(a)
    if m * n - total < 0:
        return -1
    return m * n - total

