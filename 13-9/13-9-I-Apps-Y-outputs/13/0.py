
def moves_needed(n, m):
    if n == m:
        return 0
    if n % 3 == 0 and n * 2 <= m:
        return 1 + moves_needed(n * 2, m)
    if n % 2 == 0 and n * 3 <= m:
        return 1 + moves_needed(n * 3, m)
    return -1

