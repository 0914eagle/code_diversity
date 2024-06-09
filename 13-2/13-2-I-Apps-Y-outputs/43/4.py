
def is_star(grid, row, col, size):
    # Check if the star is inside the grid
    if row < 0 or row + size > len(grid) or col < 0 or col + size > len(grid[0]):
        return False
    
    # Check if the star is completely inside the grid
    for i in range(row, row + size):
        for j in range(col, col + size):
            if grid[i][j] != '*':
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
                elif is_star(grid, row, col, 2):
                    num_stars += 2
                elif is_star(grid, row, col, 3):
                    num_stars += 3
                else:
                    return "-1"
    
    # If the number of stars is greater than the number of cells, it is impossible to draw the grid
    if num_stars > len(grid) * len(grid[0]):
        return "-1"
    
    # If the number of stars is valid, return the coordinates of the stars
    stars = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '*':
                stars.append([row, col, 1])
                grid[row][col] = '.'
    
    return str(num_stars) + "\n" + "\n".join([str(star[0]) + " " + str(star[1]) + " " + str(star[2]) for star in stars])

grid = [
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '*', '*', '*', '*', '*', '*', '.'],
    ['.', '*', '*', '*', '*', '*', '*', '.'],
    ['.', '*', '*', '*', '*', '*', '*', '.'],
    ['.', '*', '*', '*', '*', '*', '*', '.'],
    ['.', '*', '*', '*', '*', '*', '*', '.'],
    ['.', '*', '*', '*', '*', '*', '*', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.']
]

print(draw_grid(grid))

