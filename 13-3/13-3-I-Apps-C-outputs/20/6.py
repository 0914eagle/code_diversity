
def solve(n, m, subarrays):
    # Initialize the array a with all zeros
    a = [0] * n

    # Iterate over the subarrays chosen by Alyona
    for l, r in subarrays:
        # Find the mex of the current subarray
        mex = 0
        while mex in a[l:r+1]:
            mex += 1
        # Update the array a with the mex of the current subarray
        for i in range(l, r+1):
            a[i] = mex

    # Find the maximum possible minimum mex among all subarrays
    max_mex = max(a)

    return max_mex, a

