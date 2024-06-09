
def solve(n, m):
    if n == m:
        return 0
    if n > m:
        return -1

    count = 0
    while n != m:
        if n % 3 == 0:
            n //= 3
        else:
            n *= 2
        count += 1

    return count

