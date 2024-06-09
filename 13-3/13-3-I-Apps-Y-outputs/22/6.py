
def is_star(grid, row, col, size):
    # Check if the star is inside the grid
    if row < 0 or col < 0 or row + size > len(grid) or col + size > len(grid[0]):
        return False
    
    # Check if the star is completely inside the grid
    if any(grid[row + i][col + j] != '*' for i in range(size) for j in range(size)):
        return False
    
    # Check if the star is a valid star shape
    for i in range(size):
        for j in range(size):
            if i == j == size // 2:
                continue
            if grid[row + i][col + j] != '.':
                return False
    return True

def draw_grid(grid):
    # Initialize the number of stars needed
    num_stars = 0
    
    # Iterate through the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # If the current cell is a star, check if it is a valid star shape
            if grid[row][col] == '*':
                for size in range(1, min(len(grid) - row, len(grid[0]) - col) + 1):
                    if is_star(grid, row, col, size):
                        num_stars += 1
                        break
    
    # If no stars are found, return -1
    if num_stars == 0:
        return -1
    
    # Initialize the list of stars
    stars = []
    
    # Iterate through the grid again and find the stars
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # If the current cell is a star, check if it is a valid star shape
            if grid[row][col] == '*':
                for size in range(1, min(len(grid) - row, len(grid[0]) - col) + 1):
                    if is_star(grid, row, col, size):
                        stars.append((row, col, size))
                        break
    
    # Return the number of stars and the list of stars
    return num_stars, stars

