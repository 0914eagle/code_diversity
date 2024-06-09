
def pythagorean_triple(n):
    for m in range(1, n):
        for k in range(1, m):
            if m**2 + k**2 == n**2:
                return m, k
    return -1, -1

