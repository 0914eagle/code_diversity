
def get_max_points(grid_size, energy, start_x, start_y, cans):
    # Initialize a grid to keep track of the cans and their appearance times
    can_grid = [[0] * grid_size for _ in range(grid_size)]
    for can in cans:
        can_grid[can[0]][can[1]] = can[2]

    # Initialize a variable to keep track of the maximum points
    max_points = 0

    # Loop through each second of the game
    for second in range(1, max(can_grid) + 1):
        # Check if any cans appear in this second
        for i in range(grid_size):
            for j in range(grid_size):
                if can_grid[i][j] == second:
                    # If a can appears, check if Johnny5 is in the same cell
                    if i == start_x and j == start_y:
                        # If he is, collect the can and update the maximum points
                        max_points += 1
                        can_grid[i][j] = 0
                    else:
                        # If he is not, check if he is in an adjacent cell
                        for k in range(i - 1, i + 2):
                            for l in range(j - 1, j + 2):
                                if k == start_x and l == start_y and can_grid[k][l] == second:
                                    # If he is, collect the oil and update the energy
                                    energy += 1
                                    can_grid[k][l] = 0
                                    break

        # If any cans appear in this second, update the maximum points
        if any(can_grid[i][j] == second for i in range(grid_size) for j in range(grid_size)):
            max_points += 1

    return max_points

