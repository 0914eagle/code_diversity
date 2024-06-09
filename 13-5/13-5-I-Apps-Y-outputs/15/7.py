
def get_extra_bricks(H, N, M):
    # Initialize variables
    extra_2x2_bricks = 0
    extra_4x2_bricks = 0
    
    # Loop through each layer of the pyramid
    for layer in range(1, H+1):
        # Calculate the width of the layer
        width = 2*layer
        
        # Calculate the number of bricks needed for the layer
        num_bricks = width * layer
        
        # Check if the number of bricks needed is more than the number of bricks Kim has
        if num_bricks > N + M:
            # Calculate the number of extra bricks needed for the layer
            extra_bricks = num_bricks - (N + M)
            
            # Check if the extra bricks are 2x2 or 4x2
            if extra_bricks % 2 == 0:
                # Add the extra bricks to the total number of extra 2x2 bricks
                extra_2x2_bricks += extra_bricks // 2
            else:
                # Add the extra bricks to the total number of extra 4x2 bricks
                extra_4x2_bricks += extra_bricks // 2
    
    # Return the total number of extra bricks needed
    return extra_2x2_bricks, extra_4x2_bricks

def main():
    # Read the input
    H, N, M = map(int, input().split())
    
    # Call the function to get the extra bricks needed
    extra_2x2_bricks, extra_4x2_bricks = get_extra_bricks(H, N, M)
    
    # Print the output
    print(extra_2x2_bricks, extra_4x2_bricks)

if __name__ == '__main__':
    main()

