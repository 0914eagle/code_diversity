
def cake_problem(grid):
    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    max_cells = 0
    visited = set()

    # Loop through each row
    for i in range(rows):
        for j in range(cols):
            # If the current cell is empty and has not been visited before, start a new path
            if grid[i][j] == "." and (i, j) not in visited:
                # Perform a DFS to find the maximum number of cells that can be eaten in this path
                cells = dfs(grid, i, j, visited)
                max_cells = max(max_cells, cells)

    return max_cells

# Perform a DFS to find the maximum number of cells that can be eaten in a path
def dfs(grid, i, j, visited):
    # If the current cell is empty and has not been visited before, mark it as visited and continue the path
    if grid[i][j] == "." and (i, j) not in visited:
        visited.add((i, j))
        # If the current cell is on the edge of the grid, return the number of cells in the path
        if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
            return len(visited)
        # Otherwise, perform a DFS on the neighboring cells
        for new_i, new_j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            dfs(grid, new_i, new_j, visited)

    return len(visited)

