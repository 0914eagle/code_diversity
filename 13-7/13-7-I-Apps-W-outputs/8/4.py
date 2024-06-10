
def get_min_unbalancedness(grid):
    # Initialize the minimum unbalancedness to a large value
    min_unbalancedness = float('inf')
    
    # Loop through all possible colorings of the grid
    for coloring in itertools.product([0, 1], repeat=len(grid)):
        # Calculate the unbalancedness for this coloring
        unbalancedness = calculate_unbalancedness(grid, coloring)
        
        # Update the minimum unbalancedness if necessary
        if unbalancedness < min_unbalancedness:
            min_unbalancedness = unbalancedness
    
    # Return the minimum unbalancedness
    return min_unbalancedness

def calculate_unbalancedness(grid, coloring):
    # Initialize the sums of red and blue numbers to 0
    red_sum, blue_sum = 0, 0
    
    # Loop through the grid and calculate the sums of red and blue numbers
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if coloring[i * len(grid[i]) + j] == 0:
                red_sum += grid[i][j]
            else:
                blue_sum += grid[i][j]
    
    # Return the absolute difference of the sums
    return abs(red_sum - blue_sum)

def main():
    # Read the input grid from stdin
    grid = []
    for line in sys.stdin:
        grid.append(list(map(int, line.split())))
    
    # Get the minimum unbalancedness for the given grid
    min_unbalancedness = get_min_unbalancedness(grid)
    
    # Print the minimum unbalancedness
    print(min_unbalancedness)

if __name__ == '__main__':
    main()

