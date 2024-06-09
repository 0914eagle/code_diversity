
def f1(grid, direction):
    # Convert the grid to a list of lists
    grid = [list(map(int, row)) for row in grid.split()]
    
    # Get the number of rows and columns
    num_rows, num_cols = len(grid), len(grid[0])
    
    # Initialize the new grid with the same dimensions
    new_grid = [[0] * num_cols for _ in range(num_rows)]
    
    # Loop through each row and column
    for i in range(num_rows):
        for j in range(num_cols):
            # If the current cell is not empty
            if grid[i][j] != 0:
                # Find the first empty cell in the current row or column
                empty_cell = None
                for k in range(num_rows):
                    if grid[k][j] == 0:
                        empty_cell = (k, j)
                        break
                if empty_cell:
                    # Move the current cell to the empty cell
                    new_grid[empty_cell[0]][empty_cell[1]] = grid[i][j]
                    grid[i][j] = 0
    
    # Merge the cells if they are adjacent and have the same value
    for i in range(num_rows):
        for j in range(num_cols - 1):
            if grid[i][j] == grid[i][j + 1]:
                grid[i][j] *= 2
                grid[i][j + 1] = 0
    
    # Return the new grid
    return new_grid

def f2(grid, direction):
    # Convert the grid to a list of lists
    grid = [list(map(int, row)) for row in grid.split()]
    
    # Get the number of rows and columns
    num_rows, num_cols = len(grid), len(grid[0])
    
    # Initialize the new grid with the same dimensions
    new_grid = [[0] * num_cols for _ in range(num_rows)]
    
    # Loop through each row and column
    for i in range(num_rows):
        for j in range(num_cols):
            # If the current cell is not empty
            if grid[i][j] != 0:
                # Find the first empty cell in the current row or column
                empty_cell = None
                for k in range(num_rows):
                    if grid[k][j] == 0:
                        empty_cell = (k, j)
                        break
                if empty_cell:
                    # Move the current cell to the empty cell
                    new_grid[empty_cell[0]][empty_cell[1]] = grid[i][j]
                    grid[i][j] = 0
    
    # Merge the cells if they are adjacent and have the same value
    for i in range(num_rows - 1):
        for j in range(num_cols):
            if grid[i][j] == grid[i + 1][j]:
                grid[i][j] *= 2
                grid[i + 1][j] = 0
    
    # Return the new grid
    return new_grid

if __name__ == '__main__':
    grid = "2 0 0 2 4 16 8 2 2 64 32 4 1024 1024 64 0"
    direction = 0
    print(f1(grid, direction))
    print(f2(grid, direction))

