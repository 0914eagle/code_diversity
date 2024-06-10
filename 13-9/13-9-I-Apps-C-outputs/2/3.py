
def find_max_blocks(m):
    # Initialize variables
    max_blocks = 0
    max_x = 0
    
    # Iterate through possible values of X
    for x in range(1, m + 1):
        # Initialize variables
        blocks = 0
        remaining_volume = x
        
        # Iterate through possible values of the side of the block
        for side in range(1, int(x ** (1/3)) + 1):
            # Calculate the volume of the block
            volume = side ** 3
            
            # Check if the block fits in the remaining volume
            if volume <= remaining_volume:
                # Add the block to the tower
                blocks += 1
                remaining_volume -= volume
            else:
                # Break the loop and move on to the next value of X
                break
        
        # Check if the current tower has more blocks than the maximum tower
        if blocks > max_blocks:
            max_blocks = blocks
            max_x = x
    
    # Return the maximum number of blocks and the maximum value of X
    return max_blocks, max_x

def main():
    m = int(input())
    max_blocks, max_x = find_max_blocks(m)
    print(max_blocks, max_x)

if __name__ == '__main__':
    main()

