
def get_max_d(n, k, a):
    d = 0
    total = 0
    for i in range(n):
        d += 1
        total += a[i] // d
        if total > k:
            return d - 1
    return d

