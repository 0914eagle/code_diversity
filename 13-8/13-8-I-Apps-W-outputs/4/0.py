
def cakeminator(grid):
    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    count = 0
    visited = set()

    # Loop through each row and column
    for i in range(rows):
        for j in range(cols):
            # If the current cell is empty and has not been visited before, mark it as visited and increment the count
            if grid[i][j] == "." and (i, j) not in visited:
                count += 1
                visited.add((i, j))

    # Return the maximum number of cake cells that the cakeminator can eat
    return count

