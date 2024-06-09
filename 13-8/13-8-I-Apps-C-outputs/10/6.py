
def solve(n, m, subarrays):
    # Initialize the array a with all 0s
    a = [0] * n

    # Iterate over the subarrays chosen by Alyona
    for l, r in subarrays:
        # Find the minimum element in the subarray
        min_elem = min(a[l:r+1])

        # If the minimum element is 0, then set it to 1
        if min_elem == 0:
            a[l] = 1

        # Otherwise, set the minimum element to its next higher integer
        else:
            a[l] = min_elem + 1

    # Return the maximum possible minimum mex and the array a
    return max(a), a

