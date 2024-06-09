
def solve(grid):
    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    max_cells = 0

    # Loop through each row
    for i in range(rows):
        # Loop through each column
        for j in range(cols):
            # If the current cell is empty, continue to the next cell
            if grid[i][j] == ".":
                continue

            # If the current cell is an evil strawberry, mark it as visited
            grid[i][j] = "X"

            # Count the number of adjacent empty cells
            count = 0
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if 0 <= k < rows and 0 <= l < cols and grid[k][l] == ".":
                        count += 1

            # Update the maximum number of cells if necessary
            max_cells = max(max_cells, count)

    return max_cells

