
def solve(n, m):
    if n == m:
        return 0
    if n > m:
        return -1
    if m % n == 0:
        return m // n
    if n % 2 == 0 and m % (n // 2) == 0:
        return 1 + solve(n // 2, m // (n // 2))
    if n % 3 == 0 and m % (n // 3) == 0:
        return 1 + solve(n // 3, m // (n // 3))
    return -1

