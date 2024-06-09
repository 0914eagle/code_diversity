
def is_reproducible(grid):
    # Initialize a set to store the colors of the art piece
    colors = set()
    # Loop through the grid and add the colors to the set
    for row in grid:
        for color in row:
            colors.add(color)
    # Check if the set of colors is a subset of the set of all colors
    all_colors = {"R", "G", "B", "W"}
    return colors.issubset(all_colors)

