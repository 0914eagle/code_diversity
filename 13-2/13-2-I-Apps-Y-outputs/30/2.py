
def solve(n, m):
    if n == m:
        return 0
    if n > m:
        return -1
    count = 0
    while n < m:
        if m % 2 == 0:
            m //= 2
        else:
            m = m // 3 + m % 3
        count += 1
    return count

