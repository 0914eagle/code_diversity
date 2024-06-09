
def get_max_valid_sequence(blocks):
    # Sort the blocks by their values in descending order
    blocks.sort(key=lambda x: x[1], reverse=True)
    
    # Initialize the maximum valid sequence with the first block
    max_sequence = [blocks[0]]
    max_value = blocks[0][1]
    
    # Iterate over the remaining blocks
    for block in blocks[1:]:
        # If the current block has the same color as the last block in the sequence, append it to the sequence
        if block[0] == max_sequence[-1][2]:
            max_sequence.append(block)
            max_value += block[1]
        # If the current block has a different color than the last block in the sequence, check if flipping the block changes the color
        elif block[2] == max_sequence[-1][0]:
            max_sequence.append([block[2], block[1], block[0]])
            max_value += block[1]
    
    return max_value

