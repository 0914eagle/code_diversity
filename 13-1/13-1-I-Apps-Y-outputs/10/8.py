
def is_star(grid, row, col, size):
    # Check if the star is inside the grid
    if row < 0 or col < 0 or row + size > len(grid) or col + size > len(grid[0]):
        return False
    
    # Check if the star is completely inside the grid
    if any(grid[row + i][col + j] != '*' for i in range(size) for j in range(size)):
        return False
    
    # Check if the star is not overlapping with any other star
    for i in range(size):
        for j in range(size):
            if grid[row + i][col + j] == '*':
                return False
    
    return True

def draw_grid(grid):
    # Initialize the number of stars needed
    num_stars = 0
    
    # Iterate through the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # If the current cell is a star, check if it is a valid star
            if grid[row][col] == '*':
                # Check if the star is valid
                if is_star(grid, row, col, 1):
                    num_stars += 1
                    continue
                # If the star is not valid, return -1
                return -1
    
    # If all stars are valid, return the number of stars needed
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

