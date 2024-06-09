
def is_reproducible(grid):
    # Initialize a set to store the colors of the art piece
    colors = set()
    # Loop through each row of the grid
    for row in grid:
        # Loop through each cell in the row
        for cell in row:
            # Add the color of the cell to the set
            colors.add(cell)
    # Check if the set of colors is a subset of the set of all colors
    all_colors = {"R", "G", "B", "W"}
    return colors.issubset(all_colors)

