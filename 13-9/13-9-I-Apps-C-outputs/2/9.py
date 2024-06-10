
def get_max_blocks(m):
    # Initialize variables
    max_blocks = 0
    max_volume = 0
    
    # Iterate through possible values of X
    for x in range(1, m + 1):
        # Initialize variables for this value of X
        blocks = 0
        volume = 0
        
        # Iterate through possible values of the side length of the blocks
        for a in range(1, int(x**(1/3)) + 1):
            # Calculate the number of blocks that can be added with this side length
            num_blocks = int(x / a**3)
            
            # If the total number of blocks exceeds the maximum number of blocks, break
            if blocks + num_blocks > max_blocks:
                break
            
            # Add the blocks to the tower
            blocks += num_blocks
            volume += num_blocks * a**3
            
            # If the total volume exceeds the maximum volume, break
            if volume > max_volume:
                break
        
        # If the total number of blocks and volume are greater than the current maximum, update the maximum
        if blocks > max_blocks or (blocks == max_blocks and volume > max_volume):
            max_blocks = blocks
            max_volume = volume
    
    return max_blocks, max_volume

def main():
    m = int(input())
    max_blocks, max_volume = get_max_blocks(m)
    print(max_blocks, max_volume)

if __name__ == '__main__':
    main()

