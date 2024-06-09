
def get_max_points(grid_size, energy, start_x, start_y, cans):
    # Initialize a grid to keep track of the cans and their appearance times
    can_grid = [[0] * grid_size for _ in range(grid_size)]
    for can in cans:
        can_grid[can[0]][can[1]] = can[2]

    # Initialize a variable to keep track of the maximum points scored
    max_points = 0

    # Loop through each second of the game
    for second in range(1, max(can_grid) + 1):
        # Check if any cans appear in the current second
        if any(can_grid[i][j] == second for i in range(grid_size) for j in range(grid_size)):
            # If so, move to that location and collect the can
            x, y = next((i, j) for i in range(grid_size) for j in range(grid_size) if can_grid[i][j] == second)
            can_grid[x][y] = 0
            max_points += 1

        # If Johnny5 is at a location with oil, collect it and gain energy
        if any(can_grid[i][j] == 0 for i in range(grid_size) for j in range(grid_size)):
            x, y = next((i, j) for i in range(grid_size) for j in range(grid_size) if can_grid[i][j] == 0)
            can_grid[x][y] = 1
            energy += 1

    return max_points

