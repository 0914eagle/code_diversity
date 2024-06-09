
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
    for i in range(1, n + 1):
        for combination in itertools.combinations(range(n), i):
            # Check if the combination forms a rectangle
            if is_rectangle(grid, combination):
                # If it does, calculate the number of files to move
                files_to_move = len(combination)

                # If the number of files to move is less than the current minimum, update the minimum
                if files_to_move < min_files_to_move:
                    min_files_to_move = files_to_move

    return min_files_to_move

# Check if a combination of files forms a rectangle
def is_rectangle(grid, combination):
    # Get the rows and columns of the files in the combination
    rows = [grid[file // n_c][file % n_c] for file in combination]
    cols = [file // n_c for file in combination]

    # Check if the rows and columns are consecutive
    return all(row == rows[0] for row in rows) and all(col == cols[0] for col in cols)

# Test the solution
n_r, n_c, n, m = 80, 50, 3, 2
files = [75, 5, 25, 20, 50, 35, 50, 5, 25, 35]
print(solve(n_r, n_c, n, m, files))

