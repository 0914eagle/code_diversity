
def get_max_points(grid_size, start_energy, start_x, start_y, can_locations):
    # Initialize a grid to keep track of the number of points collected at each cell
    grid = [[0] * grid_size for _ in range(grid_size)]
    
    # Initialize the current position and energy
    current_x = start_x
    current_y = start_y
    energy = start_energy
    
    # Sort the can locations by their appearance time
    can_locations.sort(key=lambda x: x[2])
    
    # Loop through the can locations and move Johnny5 accordingly
    for can_x, can_y, can_time in can_locations:
        # If the can appears before Johnny5 reaches it, move Johnny5 to the can location
        if can_time < energy:
            current_x = can_x
            current_y = can_y
            energy -= 1
        # If the can appears when Johnny5 is at the same location, collect the can and gain energy
        elif current_x == can_x and current_y == can_y:
            grid[current_x][current_y] += 1
            energy += 1
        # If the can appears in an adjacent cell, collect the spilled oil and gain energy
        elif abs(current_x - can_x) + abs(current_y - can_y) == 1:
            grid[current_x][current_y] += 1
            energy += 1
    
    # Return the maximum number of points collected
    return max(sum(row) for row in grid)

