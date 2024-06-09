
def solve_2048(grid, move):
    # Convert the grid to a list of lists
    grid = [list(map(int, row)) for row in grid.split()]
    # Get the number of rows and columns
    n = len(grid)
    # Define the directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Define the move functions
    move_functions = {0: move_left, 1: move_up, 2: move_right, 3: move_down}
    # Make the move
    move_functions[move](grid)
    # Return the grid as a string
    return "\n".join(" ".join(map(str, row)) for row in grid)

def move_left(grid):
    # Loop through the rows
    for i in range(len(grid)):
        # Loop through the columns
        for j in range(len(grid[i]) - 1, -1, -1):
            # Check if the current cell is empty
            if grid[i][j] == 0:
                # Loop through the previous cells
                for k in range(j - 1, -1, -1):
                    # Check if the previous cell is not empty
                    if grid[i][k] != 0:
                        # Swap the current cell with the previous cell
                        grid[i][j], grid[i][k] = grid[i][k], grid[i][j]
                        break
            # Check if the current cell is not empty
            elif grid[i][j] != 0:
                # Loop through the previous cells
                for k in range(j - 1, -1, -1):
                    # Check if the previous cell is empty
                    if grid[i][k] == 0:
                        # Swap the current cell with the previous cell
                        grid[i][j], grid[i][k] = grid[i][k], grid[i][j]
                        break
                # Check if the current cell can merge with the previous cell
                if grid[i][j] == grid[i][j - 1]:
                    # Merge the current cell with the previous cell
                    grid[i][j - 1] *= 2
                    grid[i][j] = 0

def move_up(grid):
    # Transpose the grid
    grid = list(map(list, zip(*grid)))
    # Move left
    move_left(grid)
    # Transpose the grid back
    grid = list(map(list, zip(*grid)))

def move_right(grid):
    # Reverse the grid
    grid = [row[::-1] for row in grid]
    # Move left
    move_left(grid)
    # Reverse the grid back
    grid = [row[::-1] for row in grid]

def move_down(grid):
    # Transpose the grid
    grid = list(map(list, zip(*grid)))
    # Move right
    move_right(grid)
    # Transpose the grid back
    grid = list(map(list, zip(*grid)))


