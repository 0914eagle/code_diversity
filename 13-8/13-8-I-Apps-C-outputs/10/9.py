
def get_maximum_minimum_mex(n, m, l_list, r_list):
    a = [0] * n
    for i in range(m):
        l = l_list[i] - 1
        r = r_list[i] - 1
        for j in range(l, r + 1):
            a[j] = 1
    mex = 0
    for i in range(n):
        if a[i] == 0:
            mex += 1
    return mex, a

