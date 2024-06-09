
def solve(grid):
    # Initialize a 2D array to store the number of bombs adjacent to each empty square
    adjacent_bombs = [[0] * len(grid[0]) for _ in range(len(grid))]

    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the grid
        for j in range(len(grid[0])):
            # If the current square is a bomb, skip it
            if grid[i][j] == '#':
                continue
            # Otherwise, count the number of bombs adjacent to the current empty square
            adjacent_bombs[i][j] = count_bombs(grid, i, j)

    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the grid
        for j in range(len(grid[0])):
            # If the current square is a bomb, skip it
            if grid[i][j] == '#':
                continue
            # Otherwise, replace the empty square with the number of bombs adjacent to it
            grid[i] = grid[i][:j] + str(adjacent_bombs[i][j]) + grid[i][j+1:]

    return grid

def count_bombs(grid, i, j):
    # Initialize a counter for the number of bombs
    count = 0

    # Loop through the rows above the current row
    for k in range(i):
        # If the current square is a bomb, increment the counter
        if grid[k][j] == '#':
            count += 1

    # Loop through the columns to the left of the current column
    for k in range(j):
        # If the current square is a bomb, increment the counter
        if grid[i][k] == '#':
            count += 1

    # Loop through the rows below the current row
    for k in range(i+1, len(grid)):
        # If the current square is a bomb, increment the counter
        if grid[k][j] == '#':
            count += 1

    # Loop through the columns to the right of the current column
    for k in range(j+1, len(grid[0])):
        # If the current square is a bomb, increment the counter
        if grid[i][k] == '#':
            count += 1

    return count

