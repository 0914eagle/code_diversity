
def get_max_blocks_and_x(m):
    # Initialize variables
    max_blocks = 0
    max_x = 0
    
    # Iterate through all possible values of x
    for x in range(1, m + 1):
        # Initialize variables
        blocks = 0
        volume = 0
        
        # Iterate through all possible values of a
        for a in range(1, int(x ** (1/3)) + 1):
            # Calculate the volume of the current tower
            volume += a ** 3
            
            # If the volume is less than or equal to x, add a block
            if volume <= x:
                blocks += 1
            # Otherwise, break the loop
            else:
                break
        
        # If the current number of blocks is greater than the maximum, update the maximum
        if blocks > max_blocks:
            max_blocks = blocks
            max_x = x
    
    # Return the maximum number of blocks and x
    return max_blocks, max_x

