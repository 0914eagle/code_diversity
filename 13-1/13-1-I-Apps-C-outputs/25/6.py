
def get_max_blocks_and_x(m):
    # Initialize variables
    max_blocks = 0
    max_x = 0
    
    # Iterate through all possible values of X
    for x in range(1, m + 1):
        # Initialize variables for this value of X
        blocks = 0
        volume = 0
        
        # Iterate through all possible values of the side length of the blocks
        for a in range(1, int(m ** (1/3)) + 1):
            # Calculate the number of blocks that can be added with this side length
            num_blocks = x // (a ** 3)
            
            # If the number of blocks is positive, add them to the tower
            if num_blocks > 0:
                blocks += num_blocks
                volume += num_blocks * a ** 3
            
            # If the total volume exceeds X, break the loop
            if volume > x:
                break
        
        # If the number of blocks in the tower is greater than the current maximum, update the maximum values
        if blocks > max_blocks:
            max_blocks = blocks
            max_x = x
    
    # Return the maximum number of blocks and the maximum value of X
    return max_blocks, max_x

