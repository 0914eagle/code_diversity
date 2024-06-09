
def solve(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the result array
    result = []
    # Loop through the array and find the blocks
    for i in range(len(arr)):
        # Check if the current element is the same as the previous element
        if i > 0 and arr[i] == arr[i-1]:
            # If it is, continue the current block
            result[-1][1] += 1
        else:
            # If it is not, start a new block
            result.append([i, i])
    return result

