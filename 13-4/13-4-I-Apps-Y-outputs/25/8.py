
def is_star(grid, row, col, size):
    # Check if the star is inside the grid
    if row < 0 or col < 0 or row + size > len(grid) or col + size > len(grid[0]):
        return False
    
    # Check if the star is completely inside the grid
    if any(grid[row + i][col + j] != '*' for i in range(size) for j in range(size)):
        return False
    
    # Check if the star intersects with any other star
    for i in range(size):
        for j in range(size):
            if grid[row + i][col + j] == '*' and (i > 0 or j > 0):
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
                # Check if the star is inside the grid
                if row < 0 or col < 0 or row + 1 > len(grid) or col + 1 > len(grid[0]):
                    return -1
                
                # Check if the star is completely inside the grid
                if any(grid[row + i][col + j] != '*' for i in range(1) for j in range(1)):
                    return -1
                
                # Check if the star intersects with any other star
                for i in range(1):
                    for j in range(1):
                        if grid[row + i][col + j] == '*' and (i > 0 or j > 0):
                            return -1
                
                # If the star is possible to draw, increment the number of stars needed
                num_stars += 1
    
    # If the grid is possible to draw, return the number of stars needed
    if num_stars <= len(grid) * len(grid[0]):
        return num_stars
    
    # If the grid is not possible to draw, return -1
    return -1

