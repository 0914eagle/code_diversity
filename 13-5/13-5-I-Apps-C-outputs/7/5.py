
def get_maximal_mex(n, m, subarrays):
    a = [0] * n
    for l, r in subarrays:
        for i in range(l, r + 1):
            a[i] = 1
    mex = 0
    for i in range(n):
        if a[i] == 0:
            mex += 1
    return mex, a

