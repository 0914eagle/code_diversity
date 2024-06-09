
def solve(n_r, n_c, n, m, files):
    # Initialize a grid to represent the screen
    grid = [[0] * n_c for _ in range(n_r)]

    # Place the files on the grid
    for i in range(n):
        r, c = files[i * 2], files[i * 2 + 1]
        grid[r][c] = 1

    # Initialize the number of moves to 0
    moves = 0

    # Loop through each row of the grid
    for i in range(n_r):
        # Loop through each column of the grid
        for j in range(n_c):
            # If the current cell is a file icon, check if it's in a delete rectangle
            if grid[i][j] == 1:
                # Check if the current cell is in a delete rectangle
                if in_delete_rectangle(grid, i, j, n_r, n_c):
                    # If it is, increment the number of moves
                    moves += 1

    return moves

def in_delete_rectangle(grid, r, c, n_r, n_c):
    # Check if the current cell is in a delete rectangle
    for i in range(r, n_r):
        for j in range(c, n_c):
            if grid[i][j] == 1:
                return True
    return False

n_r, n_c, n, m = map(int, input().split())
files = list(map(int, input().split()))
print(solve(n_r, n_c, n, m, files))

