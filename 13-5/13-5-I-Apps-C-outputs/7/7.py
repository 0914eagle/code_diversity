
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
            a[i] = max(a[i], mex)

    # Find the maximum mex among all subarrays
    max_mex = max(a)

    # Return the maximum mex and the array
    return max_mex, a

