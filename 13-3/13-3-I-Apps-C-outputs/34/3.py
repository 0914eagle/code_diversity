
def get_max_points(grid_size, energy, start_x, start_y, cans):
    # Initialize a grid to keep track of the cans and their appearance times
    can_grid = [[0] * grid_size for _ in range(grid_size)]
    for can in cans:
        can_grid[can[0]][can[1]] = can[2]

    # Initialize variables to keep track of the maximum points and the current position
    max_points = 0
    current_x = start_x
    current_y = start_y

    # Sort the cans by their appearance time in ascending order
    sorted_cans = sorted(cans, key=lambda x: x[2])

    # Loop through the cans and move Johnny5 accordingly
    for can in sorted_cans:
        # If the can appears before Johnny5 reaches it, move him towards it
        if can[2] < current_x + current_y:
            # Calculate the distance between Johnny5 and the can
            distance = abs(can[0] - current_x) + abs(can[1] - current_y)

            # If Johnny5 can reach the can before it explodes, move him towards it
            if distance <= energy:
                # Update the current position and energy
                current_x = can[0]
                current_y = can[1]
                energy -= distance

                # If Johnny5 collects the can, add 1 point to the maximum points
                if can_grid[current_x][current_y] == can[2]:
                    max_points += 1
                    can_grid[current_x][current_y] = 0

            # If Johnny5 cannot reach the can before it explodes, move him away from it
            else:
                # Update the current position and energy
                current_x = can[0] + can[1]
                energy = 0

                # If Johnny5 collects the can, add 1 point to the maximum points
                if can_grid[current_x][current_y] == can[2]:
                    max_points += 1
                    can_grid[current_x][current_y] = 0

        # If the can appears after Johnny5 reaches it, move him away from it
        else:
            # Update the current position and energy
            current_x = can[0] + can[1]
            energy = 0

            # If Johnny5 collects the can, add 1 point to the maximum points
            if can_grid[current_x][current_y] == can[2]:
                max_points += 1
                can_grid[current_x][current_y] = 0

    return max_points

