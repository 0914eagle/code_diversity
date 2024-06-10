
def get_max_blocks_and_x(m):
    # Initialize variables
    max_blocks = 0
    max_x = 0
    
    # Iterate through all possible values of X
    for x in range(1, m + 1):
        # Initialize variables for this value of X
        blocks = 0
        volume = 0
        
        # Iterate through all possible values of the side of the blocks
        for side in range(1, int(m ** (1/3)) + 1):
            # Calculate the volume of the block
            volume += side ** 3
            
            # If the volume is less than or equal to X, add the block to the tower
            if volume <= x:
                blocks += 1
            else:
                break
        
        # If the number of blocks is greater than the current maximum, update the maximum values
        if blocks > max_blocks:
            max_blocks = blocks
            max_x = x
    
    # Return the maximum number of blocks and X
    return max_blocks, max_x

def main():
    m = int(input())
    max_blocks, max_x = get_max_blocks_and_x(m)
    print(max_blocks, max_x)

if __name__ == '__main__':
    main()

