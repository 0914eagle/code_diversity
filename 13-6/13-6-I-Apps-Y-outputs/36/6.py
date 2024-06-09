
def solve(arr):
    n = len(arr)
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the result
    result = []
    # Iterate through the array
    for i in range(n):
        # Check if the current element is already part of a block
        if arr[i] in result:
            continue
        # Initialize the block with the current element
        block = [arr[i]]
        # Iterate through the remaining elements
        for j in range(i+1, n):
            # Check if the current element is part of the block
            if arr[j] == arr[i]:
                # Add the element to the block
                block.append(arr[j])
                # Remove the element from the array
                arr.remove(arr[j])
        # Add the block to the result
        result.append(block)
    return result

