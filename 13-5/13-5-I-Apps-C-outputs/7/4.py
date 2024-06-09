
def solve(n, m, subarrays):
    # Initialize the array with all 0s
    a = [0] * n

    # Iterate over the subarrays
    for l, r in subarrays:
        # Find the maximum element in the subarray
        max_element = max(a[l:r+1])

        # If the maximum element is 0, then the mex is 1
        if max_element == 0:
            a[l:r+1] = [1] * (r-l+1)
        # Otherwise, find the next available number and assign it to the subarray
        else:
            for i in range(max_element+1, 10**9+1):
                if i not in a[l:r+1]:
                    a[l:r+1] = [i] * (r-l+1)
                    break

    # Return the maximum possible minimum mex and the array a
    return max(a), a

