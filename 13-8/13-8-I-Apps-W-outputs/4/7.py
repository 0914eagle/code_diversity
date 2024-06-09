
def solve(grid):
    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    count = 0
    visited = set()

    # Loop through each row
    for i in range(rows):
        # Loop through each column
        for j in range(cols):
            # If the current cell is empty and has not been visited before, mark it as visited and increment the count
            if grid[i][j] == "." and (i, j) not in visited:
                count += 1
                visited.add((i, j))

                # If the current cell is in the first or last row, mark all cells in the same column as visited
                if i in [0, rows - 1]:
                    for k in range(cols):
                        if grid[k][j] == "." and (k, j) not in visited:
                            visited.add((k, j))

                # If the current cell is in the first or last column, mark all cells in the same row as visited
                if j in [0, cols - 1]:
                    for k in range(rows):
                        if grid[i][k] == "." and (i, k) not in visited:
                            visited.add((i, k))

    return count

