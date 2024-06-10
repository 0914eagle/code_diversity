
def get_adjacent_bombs(grid, row, col):
    # Initialize a counter for the number of adjacent bombs
    num_bombs = 0
    
    # Loop through the adjacent squares and check if they are bombs
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            # Check if the current square is a bomb
            if grid[r][c] == "#":
                num_bombs += 1
    
    # Return the number of adjacent bombs
    return num_bombs

def replace_dots(grid):
    # Initialize an empty list to store the replaced grid
    replaced_grid = []
    
    # Loop through the grid and replace the . with the number of adjacent bombs
    for row in range(len(grid)):
        replaced_row = []
        for col in range(len(grid[0])):
            if grid[row][col] == ".":
                replaced_row.append(str(get_adjacent_bombs(grid, row, col)))
            else:
                replaced_row.append(grid[row][col])
        replaced_grid.append("".join(replaced_row))
    
    # Return the replaced grid
    return replaced_grid

def main():
    # Read the input grid
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    
    # Replace the . with the number of adjacent bombs
    replaced_grid = replace_dots(grid)
    
    # Print the replaced grid
    for row in replaced_grid:
        print(row)

if __name__ == '__main__':
    main()

