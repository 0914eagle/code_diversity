
def get_max_d(n, k, a):
    d = 1
    total_length = 0
    for i in range(n):
        total_length += a[i]
        if total_length > k:
            return d - 1
        d += 1
    return d

