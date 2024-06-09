
def solve(n, m):
    if n == m:
        return 0
    if n % 3 == 0 and n // 3 <= m:
        return 1 + solve(n // 3, m)
    if n % 2 == 0 and n // 2 <= m:
        return 1 + solve(n // 2, m)
    return -1

