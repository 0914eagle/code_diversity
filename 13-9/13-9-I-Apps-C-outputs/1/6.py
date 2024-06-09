
def solve(grid):
    # Initialize variables
    north_magnets = 0
    south_magnets = 0
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    # Count the number of south magnets
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "S":
                south_magnets += 1

    # Check if it is possible to place magnets such that the conditions are met
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "B" and not visited[i][j]:
                # If the cell is black and has not been visited, try to place a north magnet there
                north_magnets += 1
                visited[i][j] = True
                if not check_row(grid, visited, i, j) or not check_col(grid, visited, i, j):
                    # If it is not possible to place a north magnet in this cell, return -1
                    return -1

    # Check if there is at least one south magnet in every row and every column
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "B" and not visited[i][j]:
                # If there is a black cell that has not been visited, try to place a south magnet there
                south_magnets += 1
                visited[i][j] = True
                if not check_row(grid, visited, i, j) or not check_col(grid, visited, i, j):
                    # If it is not possible to place a south magnet in this cell, return -1
                    return -1

    # If it is possible to place magnets such that the conditions are met, return the minimum number of north magnets required
    return north_magnets

# Check if it is possible to place a north magnet in the same row as the current cell
def check_row(grid, visited, i, j):
    rows, cols = len(grid), len(grid[0])
    for k in range(cols):
        if grid[i][k] == "S" and not visited[i][k]:
            return True
    return False

# Check if it is possible to place a north magnet in the same column as the current cell
def check_col(grid, visited, i, j):
    rows, cols = len(grid), len(grid[0])
    for k in range(rows):
        if grid[k][j] == "S" and not visited[k][j]:
            return True
    return False

