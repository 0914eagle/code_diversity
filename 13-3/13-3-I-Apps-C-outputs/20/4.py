
def solve(n, m, l_r):
    # Initialize the array a with all 0s
    a = [0] * n

    # Loop through each subarray
    for l, r in l_r:
        # Find the mex of the subarray
        mex = 0
        while mex in a[l:r+1]:
            mex += 1
        # Update the array a with the mex
        for i in range(l, r+1):
            a[i] = mex

    # Find the minimum mex among all subarrays
    min_mex = min(a)

    # Return the minimum mex and the array a
    return min_mex, a

