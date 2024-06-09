
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

        # Iterate through all files to be deleted
        for j in range(n):
            # Check if the file is set to be deleted
            if i & (1 << j):
                # Get the row and column of the file
                r, c = files[j * 2], files[j * 2 + 1]

                # Check if the file is not already in the delete rectangle
                if grid[r][c] == 0:
                    # Increment the number of moves
                    moves += 1

                    # Set the file to be deleted
                    grid[r][c] = 2

        # Check if the delete rectangle contains all files to be deleted
        if all(grid[r][c] in (0, 2) for r in range(n_r) for c in range(n_c)):
            # Add the number of moves to the minimum number of moves
            min_moves = min(min_moves, moves)

    # Return the minimum number of moves
    return min_moves

