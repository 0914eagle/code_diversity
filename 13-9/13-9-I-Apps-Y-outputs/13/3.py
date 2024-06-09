
def solve(n, m):
    if n == m:
        return 0
    if n > m:
        return -1
    moves = 0
    while n < m:
        if m % 2 == 0:
            m //= 2
        else:
            m = m // 3 + m % 3
        moves += 1
    return moves

