
def moves_needed(n, m):
    if n == m:
        return 0
    if n > m:
        return -1
    if m % n == 0:
        return m // n
    if n % m == 0:
        return n // m
    return -1

