
def solve(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the result array
    result = []
    # Loop through the array and find the blocks
    for i in range(len(arr)):
        # Check if the current element is already part of a block
        if i > 0 and arr[i] == arr[i-1]:
            continue
        # Find the right boundary of the block
        j = i
        while j < len(arr)-1 and arr[j] == arr[j+1]:
            j += 1
        # Add the block to the result array
        result.append((i, j))
    return result

