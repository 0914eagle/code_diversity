
def is_reproducible(grid):
    # Check if the grid is valid
    if not grid or not all(len(row) == len(grid[0]) for row in grid):
        return "NO"
    
    # Initialize the colors dictionary
    colors = {"R": 0, "G": 0, "B": 0, "W": 0}
    
    # Loop through the grid and count the number of each color
    for row in grid:
        for col in row:
            colors[col] += 1
    
    # Check if the number of each color is even
    for color, count in colors.items():
        if count % 2 != 0:
            return "NO"
    
    # If all colors are even, the grid is reproducible
    return "YES"

