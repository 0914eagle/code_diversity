
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
        a[l:r+1] = [mex] * (r-l+1)

    # Return the maximum possible minimum mex and the array a
    return max(a), a

