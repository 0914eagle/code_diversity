
def get_extra_bricks(H, N, M):
    # Initialize variables
    extra_2x2_bricks = 0
    extra_4x2_bricks = 0
    
    # Iterate through each layer of the pyramid
    for layer in range(1, H+1):
        # Calculate the width of the layer
        width = 2*layer
        
        # Calculate the number of bricks needed for the layer
        num_bricks_needed = width * layer
        
        # Calculate the number of extra bricks needed for the layer
        extra_bricks_needed = num_bricks_needed - N - M
        
        # If the number of extra bricks needed is positive, add them to the total
        if extra_bricks_needed > 0:
            extra_2x2_bricks += extra_bricks_needed // 2
            extra_4x2_bricks += extra_bricks_needed % 2
    
    # Return the total number of extra bricks needed
    return extra_2x2_bricks, extra_4x2_bricks

def main():
    H, N, M = map(int, input().split())
    extra_2x2_bricks, extra_4x2_bricks = get_extra_bricks(H, N, M)
    print(extra_2x2_bricks, extra_4x2_bricks)

if __name__ == '__main__':
    main()

