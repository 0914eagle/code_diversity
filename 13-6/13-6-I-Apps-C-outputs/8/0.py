
def can_reproduce_art(grid):
    # Initialize a set to store the colors of the art piece
    art_colors = set()
    
    # Iterate through the grid and add the colors to the set
    for row in grid:
        for color in row:
            art_colors.add(color)
    
    # Initialize a set to store the colors that have been used in the stamp
    used_colors = set()
    
    # Iterate through the grid and check if the color of each cell can be covered by the stamp
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the color of the current cell is not in the art_colors set, return "NO"
            if grid[i][j] not in art_colors:
                return "NO"
            
            # If the color of the current cell has already been used in the stamp, continue
            if grid[i][j] in used_colors:
                continue
            
            # If the color of the current cell is not in the used_colors set, add it to the set and continue
            used_colors.add(grid[i][j])
            
            # If the color of the current cell is red, check if the colors of the adjacent cells are red, green, and blue
            if grid[i][j] == "R":
                if "R" not in used_colors and "G" not in used_colors and "B" not in used_colors:
                    return "NO"
            
            # If the color of the current cell is green, check if the colors of the adjacent cells are green, blue, and red
            if grid[i][j] == "G":
                if "G" not in used_colors and "B" not in used_colors and "R" not in used_colors:
                    return "NO"
            
            # If the color of the current cell is blue, check if the colors of the adjacent cells are blue, red, and green
            if grid[i][j] == "B":
                if "B" not in used_colors and "R" not in used_colors and "G" not in used_colors:
                    return "NO"
    
    # If all the cells have been checked and no "NO" has been returned, return "YES"
    return "YES"

