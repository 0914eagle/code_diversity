
def solve(n_r, n_c, n, m, files):
    # Initialize a grid to represent the screen
    grid = [[0] * n_c for _ in range(n_r)]

    # Populate the grid with the files to be deleted
    for i in range(n):
        r, c = files[i * 2], files[i * 2 + 1]
        grid[r][c] = 1

    # Initialize the number of moves to 0
    moves = 0

    # Loop through each row of the grid
    for i in range(n_r):
        # Loop through each column of the grid
        for j in range(n_c):
            # If the current cell is not empty and is not part of a delete rectangle, increment the number of moves
            if grid[i][j] == 1 and not is_in_rectangle(grid, i, j):
                moves += 1

    return moves

# Check if a cell is part of a delete rectangle
def is_in_rectangle(grid, r, c):
    # Loop through each cell in the grid
    for i in range(n_r):
        for j in range(n_c):
            # If the current cell is part of a delete rectangle, return True
            if grid[i][j] == 1 and i >= r and j >= c and i < r + 15 and j < c + 9:
                return True
    return False

n_r, n_c, n, m = map(int, input().split())
files = list(map(int, input().split()))
print(solve(n_r, n_c, n, m, files))

