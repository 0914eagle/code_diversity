
def get_max_valid_sequence_value(blocks):
    # Sort the blocks by their values in descending order
    blocks.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize the maximum valid sequence value to 0
    max_value = 0
    
    # Iterate over the blocks
    for i in range(len(blocks)):
        # Get the current block
        block = blocks[i]
        
        # Get the value of the current block
        value = block[1]
        
        # Check if the current block is flipped or not
        flipped = block[0] != block[2]
        
        # If the current block is not flipped, then it can be used as is
        if not flipped:
            # Add the value of the current block to the maximum valid sequence value
            max_value += value
        
        # If the current block is flipped, then it can be used as is if the previous block has the same color as the current block's color_2
        else:
            # Check if the previous block is not the first block in the sequence
            if i > 0:
                # Get the previous block
                prev_block = blocks[i - 1]
                
                # Check if the previous block has the same color as the current block's color_2
                if prev_block[1] == block[2]:
                    # Add the value of the current block to the maximum valid sequence value
                    max_value += value
        
    # Return the maximum valid sequence value
    return max_value

