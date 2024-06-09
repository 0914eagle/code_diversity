
def get_maximum_minimum_mex(n, m, subarrays):
    # Initialize the array with all zeros
    a = [0] * n

    # Loop through each subarray
    for l, r in subarrays:
        # Find the maximum value in the subarray
        max_value = max(a[l:r+1])

        # Update the array with the maximum value plus one
        for i in range(l, r+1):
            a[i] = max(a[i], max_value+1)

    # Return the maximum value in the array
    return max(a)

