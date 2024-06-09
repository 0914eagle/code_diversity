
def get_max_value(blocks):
    # Sort the blocks by their values in descending order
    blocks.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize the maximum value and the current value
    max_value = 0
    current_value = 0
    
    # Iterate through the blocks
    for block in blocks:
        # If the current value plus the value of the current block is less than or equal to the maximum value, skip the block
        if current_value + block[1] <= max_value:
            continue
        # Otherwise, add the value of the current block to the current value and update the maximum value if necessary
        current_value += block[1]
        max_value = max(max_value, current_value)
    
    # Return the maximum value
    return max_value

