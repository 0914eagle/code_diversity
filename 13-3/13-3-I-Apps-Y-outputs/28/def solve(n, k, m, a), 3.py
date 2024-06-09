
def solve(n, k, m, a):
    total = sum(a)
    if total/n >= m:
        return -1
    return m*k - total

