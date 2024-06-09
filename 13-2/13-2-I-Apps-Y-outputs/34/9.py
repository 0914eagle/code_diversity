
def solve(grid):
    # Initialize a 2D array to store the number of bombs adjacent to each empty square
    num_bombs = [[0] * len(grid[0]) for _ in range(len(grid))]

    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the grid
        for j in range(len(grid[0])):
            # If the current square is a bomb, skip it
            if grid[i][j] == '#':
                continue

            # Count the number of bombs adjacent to the current empty square
            num_bombs[i][j] = count_bombs(grid, i, j)

    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the grid
        for j in range(len(grid[0])):
            # If the current square is a bomb, skip it
            if grid[i][j] == '#':
                continue

            # Replace the current empty square with the number of bombs adjacent to it
            grid[i] = grid[i][:j] + str(num_bombs[i][j]) + grid[i][j+1:]

    return grid

def count_bombs(grid, i, j):
    # Initialize a variable to store the number of bombs adjacent to the current empty square
    num_bombs = 0

    # Loop through the rows above the current row
    for k in range(i):
        # If the current square is a bomb, increment the number of bombs
        if grid[k][j] == '#':
            num_bombs += 1

    # Loop through the columns to the left of the current column
    for k in range(j):
        # If the current square is a bomb, increment the number of bombs
        if grid[i][k] == '#':
            num_bombs += 1

    # Loop through the rows below the current row
    for k in range(i+1, len(grid)):
        # If the current square is a bomb, increment the number of bombs
        if grid[k][j] == '#':
            num_bombs += 1

    # Loop through the columns to the right of the current column
    for k in range(j+1, len(grid[0])):
        # If the current square is a bomb, increment the number of bombs
        if grid[i][k] == '#':
            num_bombs += 1

    return num_bombs

