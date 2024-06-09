
def get_maximum_disjoint_blocks(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the maximum number of blocks as 0
    max_blocks = 0
    # Initialize the current number of blocks as 0
    curr_blocks = 0
    # Initialize the starting index of the current block as 0
    start_index = 0
    # Loop through the array
    for i in range(len(arr)):
        # If the current element is greater than or equal to the previous element, it belongs to the same block
        if i > 0 and arr[i] >= arr[i-1]:
            continue
        # If the current element is less than the previous element, it belongs to a new block
        else:
            # Increment the current number of blocks
            curr_blocks += 1
            # If the current number of blocks is greater than the maximum number of blocks, update the maximum number of blocks
            if curr_blocks > max_blocks:
                max_blocks = curr_blocks
            # Reset the starting index of the current block to the current index
            start_index = i
    # Return the maximum number of blocks
    return max_blocks

