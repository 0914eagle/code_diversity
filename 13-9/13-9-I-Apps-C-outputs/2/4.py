
def get_max_blocks_and_volume(m):
    # Initialize variables
    max_blocks = 0
    max_volume = 0
    
    # Iterate through all possible volumes
    for volume in range(1, m + 1):
        # Initialize variables
        blocks = 0
        current_volume = 0
        
        # Iterate through all possible sides
        for side in range(1, int(m ** (1/3)) + 1):
            # Calculate the current volume
            current_volume += side ** 3
            
            # If the current volume is less than or equal to the required volume, add the block
            if current_volume <= volume:
                blocks += 1
            else:
                break
        
        # If the current number of blocks is greater than the maximum, update the maximum
        if blocks > max_blocks:
            max_blocks = blocks
            max_volume = volume
    
    # Return the maximum number of blocks and volume
    return max_blocks, max_volume

def main():
    m = int(input())
    max_blocks, max_volume = get_max_blocks_and_volume(m)
    print(max_blocks, max_volume)

if __name__ == '__main__':
    main()

