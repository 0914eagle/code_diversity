
def get_max_points(grid_size, start_energy, start_pos, can_locations):
    # Initialize a grid to keep track of the number of cans collected at each position
    grid = [[0] * grid_size for _ in range(grid_size)]
    
    # Initialize the current position and energy
    curr_pos = start_pos
    curr_energy = start_energy
    
    # Loop through each can location and check if Johnny5 can collect it
    for can in can_locations:
        # Check if the can is within the grid bounds
        if can[0] >= 0 and can[0] < grid_size and can[1] >= 0 and can[1] < grid_size:
            # Check if Johnny5 is at the can location
            if curr_pos == can[0:2]:
                # Collect the can and update the grid
                grid[can[0]][can[1]] += 1
                curr_energy += 1
            # Check if the can is within one move of Johnny5
            elif abs(curr_pos[0] - can[0]) + abs(curr_pos[1] - can[1]) == 1:
                # Collect the can and update the grid
                grid[can[0]][can[1]] += 1
                curr_energy += 1
            # Check if the can is within two moves of Johnny5
            elif abs(curr_pos[0] - can[0]) + abs(curr_pos[1] - can[1]) == 2:
                # Collect the can and update the grid
                grid[can[0]][can[1]] += 1
                curr_energy += 2
    
    # Calculate the maximum number of points by summing the number of cans collected at each position
    max_points = sum(map(sum, grid))
    
    return max_points

