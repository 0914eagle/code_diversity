
def solve(n, m, subarrays):
    # Initialize the array with all zeros
    a = [0] * n

    # Iterate over the subarrays
    for l, r in subarrays:
        # Find the mex of the subarray
        mex = 0
        while mex in a[l:r+1]:
            mex += 1
        # Update the array with the mex
        for i in range(l, r+1):
            a[i] = mex

    # Find the minimum mex among all subarrays
    min_mex = min(a)

    # Return the minimum mex and the array
    return min_mex, a

