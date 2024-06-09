
def is_star(grid, row, col, size):
    # Check if the star is inside the grid
    if row < 0 or col < 0 or row + size > len(grid) or col + size > len(grid[0]):
        return False
    
    # Check if the star is completely inside the grid
    if any(grid[row + i][col + j] != '*' for i in range(size) for j in range(size)):
        return False
    
    # Check if the star is not intersecting with any other star
    for i in range(row, row + size):
        for j in range(col, col + size):
            if grid[i][j] == '*' and (i, j) != (row, col):
                return False
    
    return True

def draw_grid(grid):
    # Initialize the number of stars needed
    num_stars = 0
    
    # Iterate through the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # If the current cell is a star, check if it is possible to draw it
            if grid[row][col] == '*':
                # Iterate through the possible sizes of the star
                for size in range(1, min(len(grid) - row, len(grid[0]) - col) + 1):
                    # If the star is possible to draw, break the loop and move on to the next cell
                    if is_star(grid, row, col, size):
                        break
                else:
                    # If the star is not possible to draw, return -1
                    return -1
                num_stars += 1
    
    # If all the stars are possible to draw, return the number of stars needed
    return num_stars

grid = [
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '*', '*', '*', '*', '*', '.', '.'],
    ['.', '*', '*', '*', '*', '*', '.', '.'],
    ['.', '*', '*', '*', '*', '*', '.', '.'],
    ['.', '*', '*', '*', '*', '*', '.', '.'],
    ['.', '*', '*', '*', '*', '*', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.']
]

result = draw_grid(grid)
print(result)

