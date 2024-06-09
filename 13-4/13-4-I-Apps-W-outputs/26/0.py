
def solve(desires):
    # Initialize a 2D array to store the color of each square
    grid = [[0] * 1001 for _ in range(1001)]

    # Iterate over the desires and update the color of the corresponding square
    for x, y, c in desires:
        grid[x][y] = 1 if c == "B" else -1

    # Count the number of connected components of each color
    black_components = 0
    white_components = 0
    for i in range(1001):
        for j in range(1001):
            if grid[i][j] == 1:
                black_components += 1
                dfs(grid, i, j, 1)
            elif grid[i][j] == -1:
                white_components += 1
                dfs(grid, i, j, -1)

    # Return the maximum number of desires that can be satisfied
    return max(black_components, white_components)

# DFS function to count the number of connected components of each color
def dfs(grid, i, j, color):
    # Base case: if the current square is not of the desired color, return
    if grid[i][j] != color:
        return

    # Mark the current square as visited
    grid[i][j] = 0

    # Recursive calls for the four adjacent squares
    if i > 0 and grid[i-1][j] == color:
        dfs(grid, i-1, j, color)
    if i < 1000 and grid[i+1][j] == color:
        dfs(grid, i+1, j, color)
    if j > 0 and grid[i][j-1] == color:
        dfs(grid, i, j-1, color)
    if j < 1000 and grid[i][j+1] == color:
        dfs(grid, i, j+1, color)

