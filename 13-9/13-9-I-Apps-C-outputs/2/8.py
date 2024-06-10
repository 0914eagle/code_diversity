
def get_maximum_blocks(m):
    # Initialize variables
    x = 1
    blocks = 0
    volume = 0
    
    # Loop through all possible values of x
    while x <= m:
        # Calculate the maximum number of blocks that can be added with volume x
        max_blocks = x // (x + 1)
        
        # If the current number of blocks is greater than the maximum number of blocks, break the loop
        if blocks > max_blocks:
            break
        
        # Add the current number of blocks to the total number of blocks
        blocks += max_blocks
        
        # Calculate the remaining volume
        volume = x - blocks
        
        # Increment x by 1
        x += 1
    
    # Return the maximum number of blocks and the maximum value of x
    return blocks, x - 1

def main():
    m = int(input())
    blocks, x = get_maximum_blocks(m)
    print(blocks, x)

if __name__ == '__main__':
    main()

