
def get_max_blocks_and_x(m):
    # Initialize variables
    max_blocks = 0
    max_x = 0
    
    # Iterate through all possible values of X
    for x in range(1, m + 1):
        # Initialize variables
        blocks = 0
        volume = 0
        
        # Iterate through all possible values of the side of the block
        for side in range(1, int(x ** (1/3)) + 1):
            # Calculate the volume of the block
            volume += side ** 3
            
            # Check if the volume exceeds X
            if volume > x:
                # Break the loop and move on to the next value of X
                break
            else:
                # Increment the number of blocks
                blocks += 1
        
        # Check if the current value of X results in the maximum number of blocks
        if blocks > max_blocks:
            max_blocks = blocks
            max_x = x
    
    # Return the maximum number of blocks and the maximum value of X
    return max_blocks, max_x

def main():
    m = int(input())
    max_blocks, max_x = get_max_blocks_and_x(m)
    print(max_blocks, max_x)

if __name__ == '__main__':
    main()

