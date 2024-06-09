
def solve(n_r, n_c, n, m, files):
    # Initialize a grid to represent the screen
    grid = [[0] * n_c for _ in range(n_r)]

    # Populate the grid with the files to be deleted
    for i in range(n):
        r, c = files[i * 2], files[i * 2 + 1]
        grid[r][c] = 1

    # Initialize a variable to store the minimum number of moves
    min_moves = float('inf')

    # Iterate through all possible combinations of files to be deleted
    for i in range(1 << n):
        # Initialize a variable to store the number of moves
        moves = 0

        # Initialize a variable to store the current state of the grid
        current_grid = grid[:]

        # Iterate through all files to be deleted
        for j in range(n):
            # Check if the jth file is set in the current combination
            if i & (1 << j):
                # Get the row and column of the jth file
                r, c = files[j * 2], files[j * 2 + 1]

                # Move the jth file to the top-left corner of the grid
                current_grid[0][0] = 1
                moves += 1

                # Move the jth file to the bottom-right corner of the grid
                current_grid[n_r - 1][n_c - 1] = 1
                moves += 1

        # Check if the current state of the grid is valid
        if is_valid(current_grid, m):
            # Update the minimum number of moves if necessary
            min_moves = min(min_moves, moves)

    # Return the minimum number of moves
    return min_moves

# Check if the current state of the grid is valid
def is_valid(grid, m):
    # Initialize a variable to store the number of files that should not be deleted
    num_files_not_deleted = 0

    # Iterate through the grid
    for row in grid:
        for cell in row:
            # Check if the current cell is not empty
            if cell == 1:
                # Increment the number of files that should not be deleted
                num_files_not_deleted += 1

    # Check if the number of files that should not be deleted is valid
    return num_files_not_deleted == m

# Test the solve function
n_r, n_c, n, m = 80, 50, 3, 2
files = [75, 5, 25, 20, 50, 35, 50, 5, 25, 35]
print(solve(n_r, n_c, n, m, files))

