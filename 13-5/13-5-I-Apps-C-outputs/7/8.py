
def get_maximum_minimum_mex(n, m, subarrays):
    # Initialize the array with all zeros
    a = [0] * n

    # Iterate over the subarrays
    for l, r in subarrays:
        # Get the mex of the subarray
        mex = get_mex(a[l:r+1])

        # Update the array with the mex
        for i in range(l, r+1):
            a[i] = max(a[i], mex)

    # Return the maximum minimum mex and the array
    return max(a), a

def get_mex(subarray):
    # Get the unique elements in the subarray
    unique_elements = set(subarray)

    # Iterate over the unique elements and find the first gap
    for i in range(1, len(unique_elements)):
        if i not in unique_elements:
            return i

    # If there is no gap, return the length of the subarray + 1
    return len(subarray) + 1

n, m = map(int, input().split())
subarrays = []
for _ in range(m):
    l, r = map(int, input().split())
    subarrays.append((l, r))

maximum_minimum_mex, array = get_maximum_minimum_mex(n, m, subarrays)
print(maximum_minimum_mex)
print(*array)

