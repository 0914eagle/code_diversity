
def check_lair(grid):
    # Initialize a set to store the coordinates of the corners of the lair
    lair_corners = set()
    
    # Iterate over the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is inside the lair, add its coordinates to the set of lair corners
            if grid[i][j] != 0:
                lair_corners.add((i, j))
    
    # Check if the set of lair corners has exactly 4 elements, which means that the lair has 4 corners
    if len(lair_corners) != 4:
        return "No"
    
    # Initialize a set to store the coordinates of the cells that are inside the lair
    inside_lair = set()
    
    # Iterate over the grid again
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is inside the lair, add its coordinates to the set of cells inside the lair
            if grid[i][j] != 0:
                inside_lair.add((i, j))
    
    # Check if the set of cells inside the lair has the same number of elements as the set of lair corners
    if len(inside_lair) != len(lair_corners):
        return "No"
    
    # Initialize a set to store the coordinates of the cells that are on the border of the lair
    border_lair = set()
    
    # Iterate over the grid again
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is on the border of the lair, add its coordinates to the set of cells on the border of the lair
            if grid[i][j] != 0 and (i, j) not in inside_lair:
                border_lair.add((i, j))
    
    # Check if the set of cells on the border of the lair has the same number of elements as the set of lair corners
    if len(border_lair) != len(lair_corners):
        return "No"
    
    # If all the conditions are met, return "Yes"
    return "Yes"

