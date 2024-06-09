
def get_maximum_minimal_mex(n, m, subarrays):
    # Initialize the array a with all zeros
    a = [0] * n

    # Loop through each subarray
    for l, r in subarrays:
        # Get the mex of the subarray
        mex = get_mex(a[l:r+1])

        # Update the array a with the mex
        for i in range(l, r+1):
            a[i] = mex

    # Return the maximum minimal mex and the array a
    return max(a), a

def get_mex(subarray):
    # Get the set of unique elements in the subarray
    unique_elements = set(subarray)

    # Initialize the mex to 0
    mex = 0

    # Loop through each element in the subarray
    for element in subarray:
        # If the element is not in the set of unique elements, break the loop
        if element not in unique_elements:
            break

        # Increment the mex
        mex += 1

    # Return the mex
    return mex

n, m = map(int, input().split())
subarrays = []
for _ in range(m):
    l, r = map(int, input().split())
    subarrays.append((l, r))

maximum_minimal_mex, array = get_maximum_minimal_mex(n, m, subarrays)
print(maximum_minimal_mex)
print(*array)

