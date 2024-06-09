
def get_extra_bricks(h, n, m):
    # Initialize variables
    extra_2x2_bricks = 0
    extra_4x2_bricks = 0
    
    # Iterate through each layer of the pyramid
    for i in range(1, h + 1):
        # Calculate the width of the layer
        width = 2 * i
        
        # Calculate the number of bricks needed for the layer
        num_bricks = width * i
        
        # Check if the layer can be completed with the given bricks
        if num_bricks <= n:
            # Subtract the number of bricks used from the total number of bricks
            n -= num_bricks
        else:
            # Calculate the number of extra bricks needed for the layer
            extra_bricks = num_bricks - n
            
            # Add the extra bricks to the total number of extra bricks
            extra_2x2_bricks += extra_bricks // 2
            extra_4x2_bricks += extra_bricks % 2
            
            # Subtract the number of bricks used from the total number of bricks
            n = 0
    
    # Return the total number of extra bricks needed
    return extra_2x2_bricks, extra_4x2_bricks

def main():
    # Read the input
    h, n, m = map(int, input().split())
    
    # Call the function to get the extra bricks needed
    extra_2x2_bricks, extra_4x2_bricks = get_extra_bricks(h, n, m)
    
    # Print the output
    print(extra_2x2_bricks, extra_4x2_bricks)

if __name__ == '__main__':
    main()

