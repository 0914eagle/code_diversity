
def get_extra_bricks(H, N, M):
    # Initialize variables
    extra_2x2_bricks = 0
    extra_4x2_bricks = 0
    
    # Iterate through each layer of the pyramid
    for layer in range(1, H+1):
        # Calculate the width of the layer
        width = 2*layer
        
        # Calculate the number of bricks needed for the layer
        num_bricks = width * (width + 1) // 2
        
        # Check if the layer can be completed with the given bricks
        if num_bricks <= N:
            # Subtract the number of bricks used from the total number of bricks
            N -= num_bricks
        else:
            # Calculate the number of extra bricks needed for the layer
            extra_bricks = num_bricks - N
            
            # Add the extra bricks to the total number of extra bricks
            extra_2x2_bricks += extra_bricks // 2
            extra_4x2_bricks += extra_bricks % 2
            
            # Set the number of bricks to 0 for the next layer
            N = 0
    
    # Return the total number of extra bricks needed
    return extra_2x2_bricks, extra_4x2_bricks

def main():
    # Read the input
    H, N, M = map(int, input().split())
    
    # Calculate the extra bricks needed
    extra_2x2_bricks, extra_4x2_bricks = get_extra_bricks(H, N, M)
    
    # Print the output
    print(extra_2x2_bricks, extra_4x2_bricks)

if __name__ == '__main__':
    main()

