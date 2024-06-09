
def get_max_area(grid, r1, c1, r2, c2):
    # Initialize the maximum area to 0
    max_area = 0

    # Loop through the rows and columns of the sub-rectangle
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            # Check if the current cell is part of a Nanosoft logo
            if grid[i][j] == "R" and grid[i][j + 1] == "G" and grid[i][j + 2] == "G" and grid[i][j + 3] == "B":
                # Calculate the area of the sub-square
                area = (j - c1 + 1) * (i - r1 + 1)

                # Update the maximum area if necessary
                max_area = max(max_area, area)

    # Return the maximum area
    return max_area

