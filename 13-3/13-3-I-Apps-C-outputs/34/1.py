
def get_max_points(grid_size, start_energy, start_position, can_locations):
    # Initialize a grid to keep track of the number of points collected at each position
    grid = [[0] * grid_size for _ in range(grid_size)]
    
    # Initialize the current position and energy
    current_position = start_position
    energy = start_energy
    
    # Sort the can locations by their appearance time
    can_locations.sort(key=lambda x: x[2])
    
    # Loop through the can locations
    for can_location in can_locations:
        # Calculate the distance between the current position and the can location
        distance = abs(can_location[0] - current_position[0]) + abs(can_location[1] - current_position[1])
        
        # If the distance is less than or equal to the current energy, collect the can and move to the can location
        if distance <= energy:
            grid[can_location[0]][can_location[1]] += 1
            current_position = (can_location[0], can_location[1])
            energy -= distance
        
        # If the distance is greater than the current energy, collect the oil from the adjacent cells and move to the can location
        else:
            for i in range(max(0, current_position[0] - 1), min(grid_size, current_position[0] + 2)):
                for j in range(max(0, current_position[1] - 1), min(grid_size, current_position[1] + 2)):
                    if grid[i][j] > 0:
                        energy += 1
                        grid[i][j] -= 1
            current_position = (can_location[0], can_location[1])
    
    # Return the maximum number of points collected
    return max(max(row) for row in grid)

