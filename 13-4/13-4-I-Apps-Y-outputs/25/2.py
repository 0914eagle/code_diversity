
def is_star(grid, row, col, size):
    # Check if the star is inside the grid
    if row < 0 or col < 0 or row + size > len(grid) or col + size > len(grid[0]):
        return False
    
    # Check if the star is completely inside the grid
    if any(grid[row + i][col + j] != '*' for i in range(size) for j in range(size)):
        return False
    
    # Check if the star is not overlapping with any other star
    for i in range(row, row + size):
        for j in range(col, col + size):
            if grid[i][j] == '*' and (i, j) != (row, col):
                return False
    
    return True

def draw_grid(grid):
    # Initialize the number of stars needed to draw the grid
    num_stars = 0
    
    # Iterate through the grid and check if each cell is a star
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '*':
                # Check if the star is valid
                if not is_star(grid, row, col, 1):
                    return -1
                num_stars += 1
    
    # If all cells are stars, return the number of stars needed
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

