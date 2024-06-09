
def get_maximum_minimum_mex(n, m, subarrays):
    # Initialize the array with all zeros
    array = [0] * n

    # Loop through each subarray
    for l, r in subarrays:
        # Get the mex of the subarray
        mex = get_mex(array[l:r+1])

        # Update the array with the mex
        for i in range(l, r+1):
            array[i] = mex

    # Return the maximum minimum mex and the array
    return max(array), array

def get_mex(subarray):
    # Get the unique elements in the subarray
    unique_elements = set(subarray)

    # Initialize the mex to 0
    mex = 0

    # Loop through each unique element
    for element in unique_elements:
        # If the element is not in the subarray, return the current mex
        if element not in subarray:
            return mex
        # Otherwise, increment the mex
        else:
            mex += 1

    # If all elements are in the subarray, return the maximum possible mex
    return mex

n, m = map(int, input().split())
subarrays = []
for _ in range(m):
    l, r = map(int, input().split())
    subarrays.append((l, r))

maximum_minimum_mex, array = get_maximum_minimum_mex(n, m, subarrays)
print(maximum_minimum_mex)
print(*array)

