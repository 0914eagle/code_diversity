
def solve(n, m, l_r):
    # Initialize the array a with all zeros
    a = [0] * n

    # Loop through each subarray
    for l, r in l_r:
        # Find the mex of the subarray
        mex = 0
        while mex in a[l:r+1]:
            mex += 1
        # Update the array a with the mex
        for i in range(l, r+1):
            a[i] = max(a[i], mex)

    # Find the maximum possible minimum mex
    mex = 0
    while mex in a:
        mex += 1

    return [mex, a]

