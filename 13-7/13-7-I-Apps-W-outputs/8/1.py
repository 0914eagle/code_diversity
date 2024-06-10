
def get_min_unbalancedness(grid):
    # Initialize the minimum unbalancedness as a large number
    min_unbalancedness = 1000
    
    # Loop through all possible colorings of the grid
    for coloring in itertools.product([0, 1], repeat=len(grid)):
        # Calculate the unbalancedness for the current coloring
        unbalancedness = calculate_unbalancedness(grid, coloring)
        
        # If the current unbalancedness is smaller than the minimum unbalancedness, update the minimum unbalancedness
        if unbalancedness < min_unbalancedness:
            min_unbalancedness = unbalancedness
    
    # Return the minimum unbalancedness
    return min_unbalancedness

def calculate_unbalancedness(grid, coloring):
    # Initialize the sum of red numbers and the sum of blue numbers as 0
    red_sum, blue_sum = 0, 0
    
    # Loop through all squares in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current square is red, add its value to the red sum
            if coloring[i * len(grid[0]) + j] == 0:
                red_sum += grid[i][j]
            # If the current square is blue, add its value to the blue sum
            else:
                blue_sum += grid[i][j]
    
    # Return the absolute difference of the red sum and the blue sum
    return abs(red_sum - blue_sum)

def main():
    # Read the input grid from stdin
    grid = []
    for _ in range(int(input())):
        grid.append(list(map(int, input().split())))
    
    # Calculate the minimum unbalancedness for the input grid
    min_unbalancedness = get_min_unbalancedness(grid)
    
    # Print the minimum unbalancedness
    print(min_unbalancedness)

if __name__ == '__main__':
    main()

