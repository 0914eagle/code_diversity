
def get_adjacent_bombs(grid, row, col):
    # Initialize a count of adjacent bombs to 0
    count = 0
    
    # Check if the current square has a bomb
    if grid[row][col] == '#':
        count += 1
    
    # Check if the square above the current square has a bomb
    if row > 0 and grid[row-1][col] == '#':
        count += 1
    
    # Check if the square below the current square has a bomb
    if row < len(grid) - 1 and grid[row+1][col] == '#':
        count += 1
    
    # Check if the square to the left of the current square has a bomb
    if col > 0 and grid[row][col-1] == '#':
        count += 1
    
    # Check if the square to the right of the current square has a bomb
    if col < len(grid[0]) - 1 and grid[row][col+1] == '#':
        count += 1
    
    # Check if the square diagonally above and to the left of the current square has a bomb
    if row > 0 and col > 0 and grid[row-1][col-1] == '#':
        count += 1
    
    # Check if the square diagonally above and to the right of the current square has a bomb
    if row > 0 and col < len(grid[0]) - 1 and grid[row-1][col+1] == '#':
        count += 1
    
    # Check if the square diagonally below and to the left of the current square has a bomb
    if row < len(grid) - 1 and col > 0 and grid[row+1][col-1] == '#':
        count += 1
    
    # Check if the square diagonally below and to the right of the current square has a bomb
    if row < len(grid) - 1 and col < len(grid[0]) - 1 and grid[row+1][col+1] == '#':
        count += 1
    
    return count

def replace_empty_squares(grid):
    # Initialize a new grid with the same dimensions as the original grid
    new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    
    # Loop through each row and column of the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # If the current square is empty, replace it with the number of adjacent bombs
            if grid[row][col] == '.':
                new_grid[row][col] = str(get_adjacent_bombs(grid, row, col))
            # Otherwise, keep the current value
            else:
                new_grid[row][col] = grid[row][col]
    
    return new_grid

def main():
    # Read the dimensions of the grid and the grid itself from standard input
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    
    # Replace the empty squares with the number of adjacent bombs
    new_grid = replace_empty_squares(grid)
    
    # Print the new grid
    for row in new_grid:
        print(''.join(row))

if __name__ == '__main__':
    main()

