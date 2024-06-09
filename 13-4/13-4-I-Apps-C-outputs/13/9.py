
def solve(A1, m):
    n = 1
    while True:
        d = m - A1
        if d > 0 and d not in [A1, n]:
            A1 += d
            n += 1
        else:
            break
    return n

