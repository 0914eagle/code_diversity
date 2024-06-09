
def can_reproduce_art(art_grid):
    # Initialize a set to store the colors that have been used
    used_colors = set()
    # Loop through each row of the art grid
    for row in art_grid:
        # Loop through each cell in the row
        for cell in row:
            # If the cell is not white, add it to the set of used colors
            if cell != "W":
                used_colors.add(cell)
    # If the set of used colors is not equal to the set of all colors, return "NO"
    if len(used_colors) != 4:
        return "NO"
    # Otherwise, return "YES"
    return "YES"

