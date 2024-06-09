
def solve(n_r, n_c, n, m, files):
    # Initialize a grid to represent the screen
    grid = [[0] * n_c for _ in range(n_r)]

    # Populate the grid with the files to be deleted
    for i in range(n):
        r, c = files[i * 2], files[i * 2 + 1]
        grid[r][c] = 1

    # Initialize a variable to store the minimum number of files to move
    min_files_to_move = float('inf')

    # Iterate through all possible combinations of files to move
    for files_to_move in combinations(range(n), n - m):
        # Initialize a variable to store the number of files moved
        num_files_moved = 0

        # Iterate through the files to be deleted
        for i in range(n):
            # If the file is not in the combination of files to move, skip it
            if i not in files_to_move:
                continue

            # Increment the number of files moved
            num_files_moved += 1

            # Update the grid to reflect the movement of the file
            r, c = files[i * 2], files[i * 2 + 1]
            grid[r][c] = 0

        # Check if the combination of files to move forms a rectangle
        if is_rectangle(grid, n_r, n_c, files_to_move):
            # If it does, update the minimum number of files to move
            min_files_to_move = min(min_files_to_move, num_files_moved)

    # Return the minimum number of files to move
    return min_files_to_move

# Function to check if a combination of files forms a rectangle
def is_rectangle(grid, n_r, n_c, files_to_move):
    # Initialize a variable to store the number of rows and columns spanned
    num_rows, num_cols = 0, 0

    # Iterate through the files to be moved
    for i in files_to_move:
        # Get the row and column of the file
        r, c = files[i * 2], files[i * 2 + 1]

        # Update the number of rows and columns spanned
        num_rows = max(num_rows, r + 1)
        num_cols = max(num_cols, c + 1)

    # Check if the number of rows and columns spanned is equal to the number of rows and columns in the grid
    return num_rows == n_r and num_cols == n_c

# Function to get all possible combinations of a set of items
def combinations(items, r):
    if r == 0:
        yield []
    else:
        for i in range(len(items)):
            for c in combinations(items[i+1:], r-1):
                yield [items[i]] + c

# Test the solve function
n_r, n_c, n, m = 80, 50, 3, 2
files = [75, 5, 25, 20, 50, 35, 50, 5, 25, 35]
print(solve(n_r, n_c, n, m, files))

