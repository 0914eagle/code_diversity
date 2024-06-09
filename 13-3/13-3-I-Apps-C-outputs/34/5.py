
def get_max_points(grid_size, energy, start_x, start_y, can_locations):
    # Initialize a grid to keep track of the cans and their timestamps
    can_grid = [[0] * grid_size for _ in range(grid_size)]
    for can_location in can_locations:
        can_grid[can_location[0]][can_location[1]] = can_location[2]

    # Initialize the current position and timestamp
    current_x = start_x
    current_y = start_y
    timestamp = 0

    # Initialize the maximum number of points
    max_points = 0

    # Loop through the can locations and calculate the maximum number of points
    for can_location in can_locations:
        # Calculate the time difference between the current timestamp and the timestamp of the current can
        time_diff = can_location[2] - timestamp

        # If the time difference is positive, move Johnny5 in the appropriate direction for that time difference
        if time_diff > 0:
            # Calculate the number of seconds Johnny5 can move in that time difference
            seconds_moved = min(time_diff, energy)

            # Move Johnny5 in the appropriate direction for that time difference
            if current_x + seconds_moved < grid_size:
                current_x += seconds_moved
            elif current_y + seconds_moved < grid_size:
                current_y += seconds_moved
            elif current_x - seconds_moved >= 0:
                current_x -= seconds_moved
            else:
                current_y -= seconds_moved

            # Update the timestamp and energy
            timestamp += seconds_moved
            energy -= seconds_moved

        # If the current can is at the current position of Johnny5, collect the can and update the maximum number of points
        if current_x == can_location[0] and current_y == can_location[1]:
            max_points += 1
            can_grid[current_x][current_y] = 0

    # Return the maximum number of points
    return max_points

