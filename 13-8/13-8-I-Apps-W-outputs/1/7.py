
def check_zombie_lair(grid):
    # Initialize a set to store the x and y coordinates of the lair
    lair_coords = set()
    
    # Loop through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is part of the lair, add its coordinates to the set
            if grid[i][j] != 0:
                lair_coords.add((i, j))
    
    # Check if the lair is rectangular
    if len(lair_coords) != 4:
        return "No"
    
    # Sort the coordinates of the lair
    sorted_coords = sorted(lair_coords)
    
    # Check if the lair is contained inside the grid
    if not (0 <= sorted_coords[0][0] < sorted_coords[1][0] <= len(grid) and
            0 <= sorted_coords[0][1] < sorted_coords[3][1] <= len(grid[0])):
        return "No"
    
    # Check if the levels of Zombie Contamination match the lair
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is part of the lair, check its level of Zombie Contamination
            if (i, j) in lair_coords:
                if grid[i][j] != 2:
                    return "No"
            # If the current cell is not part of the lair, check its level of Zombie Contamination
            else:
                if grid[i][j] != 0:
                    return "No"
    
    # If all checks pass, return "Yes"
    return "Yes"

