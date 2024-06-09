
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
            # If the current cell is an asterisk, check if it forms a star
            if grid[row][col] == '*':
                # Check if the star is size 1
                if is_star(grid, row, col, 1):
                    num_stars += 1
                    print(row, col, 1)
                # Check if the star is size 2
                elif is_star(grid, row, col, 2):
                    num_stars += 1
                    print(row, col, 2)
                # Check if the star is size 3
                elif is_star(grid, row, col, 3):
                    num_stars += 1
                    print(row, col, 3)
    
    return num_stars

n, m = map(int, input().split())
grid = [input() for _ in range(n)]
num_stars = draw_grid(grid)
print(num_stars)

