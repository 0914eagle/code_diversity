
def pythagorean_triple(n):
    for m in range(1, n*1000):
        k = (m**2 - n**2) // 2
        if m**2 + k**2 == n**2:
            return m, k
    return -1, -1

