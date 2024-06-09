
def get_maximum_minimal_mex(n, m, subarrays):
    a = [0] * n
    for l, r in subarrays:
        for i in range(l, r + 1):
            a[i] += 1
    return max(a)

