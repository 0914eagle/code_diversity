
def solve(desires):
    # Initialize a 2D array to store the color of each square
    grid = [[0] * 1001 for _ in range(1001)]

    # Iterate over the desires and paint the corresponding squares
    for x, y, color in desires:
        grid[x][y] = 1 if color == "B" else -1

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

# Depth-first search function to count the number of connected components
def dfs(grid, i, j, color):
    # Base case: if the current square is already painted with the same color, return
    if grid[i][j] == color:
        return

    # Paint the current square with the given color
    grid[i][j] = color

    # Recursive case: explore the surrounding squares
    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
        if 0 <= x < 1001 and 0 <= y < 1001 and grid[x][y] != color:
            dfs(grid, x, y, color)

