
def read_grid():
    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(list(map(int, input().split())))
    return H, W, grid

def paint_grid(grid):
    # Initialize the sums of red and blue numbers
    red_sum, blue_sum = 0, 0
    
    # Iterate through the grid and paint the squares
    for i in range(H):
        for j in range(W):
            if i % 2 == 0:
                red_sum += grid[i][j]
            else:
                blue_sum += grid[i][j]
    
    # Return the difference between the two sums
    return abs(red_sum - blue_sum)

def travel_grid(grid):
    # Initialize the current position and the minimum unbalancedness
    current_position = (0, 0)
    min_unbalancedness = float('inf')
    
    # Iterate through the grid and travel from (1, 1) to (H, W)
    while current_position != (H-1, W-1):
        # Get the current unbalancedness
        unbalancedness = paint_grid(grid)
        
        # Update the minimum unbalancedness if necessary
        if unbalancedness < min_unbalancedness:
            min_unbalancedness = unbalancedness
        
        # Move to the next position
        if current_position[0] == H-1:
            current_position = (0, current_position[1] + 1)
        else:
            current_position = (current_position[0] + 1, current_position[1])
    
    # Return the minimum unbalancedness
    return min_unbalancedness

if __name__ == '__main__':
    H, W, grid = read_grid()
    print(travel_grid(grid))

