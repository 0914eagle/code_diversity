
def get_max_blocks_and_x(m):
    # Initialize variables
    max_blocks = 0
    max_x = 0
    
    # Iterate through all possible values of X
    for x in range(1, m + 1):
        # Initialize variables for this value of X
        blocks = 0
        volume = 0
        
        # Iterate through all possible values of the side of the block
        for side in range(1, int(m ** (1/3)) + 1):
            # Calculate the volume of the block
            volume += side ** 3
            
            # If the volume is less than or equal to X, add the block to the tower
            if volume <= x:
                blocks += 1
            # Otherwise, break the loop and move on to the next value of X
            else:
                break
        
        # If the number of blocks in this tower is greater than the maximum, update the maximum
        if blocks > max_blocks:
            max_blocks = blocks
            max_x = x
    
    # Return the maximum number of blocks and the maximum value of X
    return max_blocks, max_x

