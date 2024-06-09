
def get_max_points(grid_size, start_energy, start_x, start_y, can_locations):
    # Initialize a grid to keep track of the number of points collected at each cell
    grid = [[0] * grid_size for _ in range(grid_size)]
    
    # Initialize the current energy and time
    energy = start_energy
    time = 0
    
    # Loop through each can location and the time it appears
    for can_x, can_y, can_time in can_locations:
        # If the can appears before Johnny5 reaches it, collect the can and gain energy
        if can_time <= time:
            grid[can_x][can_y] += 1
            energy += 1
        # If the can appears after Johnny5 reaches it, collect the can and gain energy if it is in an adjacent cell
        else:
            for x_diff in range(-1, 2):
                for y_diff in range(-1, 2):
                    if 0 <= can_x + x_diff < grid_size and 0 <= can_y + y_diff < grid_size:
                        if grid[can_x + x_diff][can_y + y_diff] == 0:
                            grid[can_x + x_diff][can_y + y_diff] += 1
                            energy += 1
    
    # Return the maximum number of points collected
    return max(sum(row) for row in grid)

