
def solve_tomb_puzzle(n, m, floorplan):
    # Initialize a list to store the gargoyle positions
    gargoyle_positions = []

    # Iterate through the floorplan and find the gargoyles
    for i in range(n):
        for j in range(m):
            if floorplan[i][j] == "V" or floorplan[i][j] == "H":
                gargoyle_positions.append((i, j))

    # If there are no gargoyles, return -1
    if not gargoyle_positions:
        return -1

    # Initialize a list to store the mirror positions
    mirror_positions = []

    # Iterate through the floorplan and find the mirrors
    for i in range(n):
        for j in range(m):
            if floorplan[i][j] == "/" or floorplan[i][j] == "\\":
                mirror_positions.append((i, j))

    # If there are no mirrors, return -1
    if not mirror_positions:
        return -1

    # Initialize a list to store the obstacle positions
    obstacle_positions = []

    # Iterate through the floorplan and find the obstacles
    for i in range(n):
        for j in range(m):
            if floorplan[i][j] == "#":
                obstacle_positions.append((i, j))

    # If there are no obstacles, return -1
    if not obstacle_positions:
        return -1

    # Initialize a list to store the solution
    solution = []

    # Iterate through the gargoyles and mirrors and find the minimum number of gargoyles that need to be rotated
    for gargoyle in gargoyle_positions:
        for mirror in mirror_positions:
            # Check if the gargoyle and mirror are in the same row or column
            if gargoyle[0] == mirror[0] or gargoyle[1] == mirror[1]:
                # Check if the gargoyle and mirror are not blocked by an obstacle
                if not any(obstacle_position in [(gargoyle[0], mirror[1]), (mirror[0], gargoyle[1])] for obstacle_position in obstacle_positions):
                    # Add the gargoyle to the solution
                    solution.append(gargoyle)
                    break

    # Return the length of the solution
    return len(solution)

