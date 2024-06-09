
def get_max_value(blocks):
    # Sort the blocks by their values in descending order
    blocks.sort(key=lambda x: x[1], reverse=True)
    # Initialize the maximum value to 0
    max_value = 0
    # Loop through the blocks
    for i in range(len(blocks)):
        # Get the current block
        block = blocks[i]
        # Get the value of the current block
        value = block[1]
        # Check if the current block is flipped or not
        flipped = block[0] != block[2]
        # If the current block is not flipped, add its value to the maximum value
        if not flipped:
            max_value += value
        # If the current block is flipped, add half of its value to the maximum value
        else:
            max_value += value // 2
    # Return the maximum value
    return max_value

