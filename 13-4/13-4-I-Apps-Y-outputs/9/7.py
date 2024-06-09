
def solve(arr):
    n = len(arr)
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the result with the first element
    result = []
    current_sum = arr[0]
    current_block = [0]
    for i in range(1, n):
        # If the current element is equal to the previous element, add it to the current block
        if arr[i] == arr[i-1]:
            current_block.append(i)
            current_sum += arr[i]
        # If the current element is not equal to the previous element, start a new block
        else:
            result.append(current_block)
            current_block = [i]
            current_sum = arr[i]
    # Add the last block to the result
    result.append(current_block)
    return result

