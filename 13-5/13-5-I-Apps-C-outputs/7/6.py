
def solve(n, m, subarrays):
    # Initialize the array a with all zeros
    a = [0] * n

    # Iterate over the subarrays chosen by Alyona
    for l, r in subarrays:
        # Find the mex of the subarray
        mex = 0
        while mex in a[l:r+1]:
            mex += 1
        # Update the array a with the mex
        for i in range(l, r+1):
            a[i] = max(a[i], mex)

    # Find the maximum possible minimum mex
    min_mex = max(a)

    return min_mex, a

