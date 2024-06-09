
def is_reproducible(grid):
    # Initialize a set to store the colors of the art piece
    art_colors = set()
    
    # Loop through the grid and add the colors to the set
    for row in grid:
        for color in row:
            art_colors.add(color)
    
    # Initialize a set to store the colors of the reproduced grid
    reproduced_colors = set()
    
    # Loop through the grid and add the colors to the set
    for row in grid:
        for color in row:
            reproduced_colors.add(color)
    
    # Check if the sets are equal
    if art_colors == reproduced_colors:
        return "YES"
    else:
        return "NO"

