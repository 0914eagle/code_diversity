
def get_max_value(blocks):
    # Sort the blocks by their values in descending order
    blocks.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize the maximum value of the valid sequence
    max_value = 0
    
    # Iterate over the blocks
    for i in range(len(blocks)):
        # Get the current block
        block = blocks[i]
        
        # If the block is not used yet, consider using it in the valid sequence
        if block[2] == 0:
            # Get the value of the block
            value = block[1]
            
            # If the block is not the first block in the sequence, consider flipping it
            if i > 0:
                # Get the previous block
                prev_block = blocks[i - 1]
                
                # If the previous block is not used yet and its right color is the same as the current block's left color, flip the current block
                if prev_block[2] == 0 and prev_block[0] == block[2]:
                    value += block[1]
                    block[2] = 1
            
            # If the block is not the last block in the sequence, consider flipping it
            if i < len(blocks) - 1:
                # Get the next block
                next_block = blocks[i + 1]
                
                # If the next block is not used yet and its left color is the same as the current block's right color, flip the current block
                if next_block[2] == 0 and next_block[1] == block[0]:
                    value += block[1]
                    block[2] = 1
            
            # Update the maximum value of the valid sequence
            max_value = max(max_value, value)
    
    # Return the maximum value of the valid sequence
    return max_value

