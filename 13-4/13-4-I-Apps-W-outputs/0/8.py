
def pythagorean_triple(n):
    for m in range(1, n * 10 ** 18):
        k = (m ** 2 - n ** 2) // 2
        if m * m + n * n == k * k:
            return [m, k]
    return [-1, -1]

