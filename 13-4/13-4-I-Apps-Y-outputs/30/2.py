
def solve_2048(grid, move):
    # Convert the grid to a list of lists
    grid = [list(map(int, row)) for row in grid.split()]
    # Get the number of rows and columns
    n = len(grid)
    # Define the directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Define the move function
    def move_left(grid):
        for i in range(n):
            grid[i] = [0] * n
            for j in range(n):
                if grid[i][j] != 0:
                    grid[i][j-1] += grid[i][j]
                    grid[i][j] = 0
        return grid
    def move_right(grid):
        for i in range(n):
            grid[i] = [0] * n
            for j in range(n):
                if grid[i][n-j-1] != 0:
                    grid[i][n-j-1+1] += grid[i][n-j-1]
                    grid[i][n-j-1] = 0
        return grid
    def move_up(grid):
        for j in range(n):
            grid[j] = [0] * n
            for i in range(n):
                if grid[i][j] != 0:
                    grid[i-1][j] += grid[i][j]
                    grid[i][j] = 0
        return grid
    def move_down(grid):
        for j in range(n):
            grid[j] = [0] * n
            for i in range(n):
                if grid[n-i-1][j] != 0:
                    grid[n-i-1+1][j] += grid[n-i-1][j]
                    grid[n-i-1][j] = 0
        return grid
    # Make the move
    if move == 0:
        grid = move_left(grid)
    elif move == 1:
        grid = move_up(grid)
    elif move == 2:
        grid = move_right(grid)
    else:
        grid = move_down(grid)
    # Return the updated grid
    return grid

