
def get_max_blocks(m):
    # Initialize variables
    max_blocks = 0
    max_x = 0
    
    # Iterate through possible values of x
    for x in range(1, m + 1):
        # Initialize variables for this value of x
        blocks = 0
        volume = 0
        
        # Iterate through possible values of the side of the block
        for side in range(1, int(m ** (1/3)) + 1):
            # Calculate the volume of the block
            volume += side ** 3
            
            # If the volume is less than or equal to x, add the block to the tower
            if volume <= x:
                blocks += 1
            else:
                break
        
        # If the number of blocks is greater than the current maximum, update the maximum
        if blocks > max_blocks:
            max_blocks = blocks
            max_x = x
    
    # Return the maximum number of blocks and the maximum x
    return max_blocks, max_x

def main():
    m = int(input())
    max_blocks, max_x = get_max_blocks(m)
    print(max_blocks, max_x)

if __name__ == '__main__':
    main()

