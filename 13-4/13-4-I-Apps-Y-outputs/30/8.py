
def solve_2048(grid, move):
    # Convert the grid to a list of lists
    grid = [list(map(int, row)) for row in grid.split()]
    # Get the number of rows and columns
    n = len(grid)
    # Define the directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Define the resulting grid
    result = [[0] * n for _ in range(n)]
    # Iterate over the rows and columns
    for i in range(n):
        for j in range(n):
            # Check if the current cell is empty
            if grid[i][j] == 0:
                continue
            # Get the current cell value
            value = grid[i][j]
            # Get the direction of the move
            direction = directions[move]
            # Get the new row and column indices
            new_i = i + direction[0]
            new_j = j + direction[1]
            # Check if the new cell is out of bounds
            if new_i < 0 or new_i >= n or new_j < 0 or new_j >= n:
                continue
            # Check if the new cell is empty
            if result[new_i][new_j] == 0:
                result[new_i][new_j] = value
                continue
            # Check if the new cell has the same value
            if result[new_i][new_j] == value:
                result[new_i][new_j] = value * 2
                continue
            # Merge the cells
            result[new_i][new_j] = value
            result[i][j] = 0
    # Return the resulting grid
    return result

