
def is_star(grid, row, col, size):
    # Check if the cell at (row, col) is a center of a star of the given size
    if grid[row][col] != '*':
        return False
    for i in range(row - size + 1, row + size):
        for j in range(col - size + 1, col + size):
            if i == row and j == col:
                continue
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return False
            if grid[i][j] != '.':
                return False
    return True

def draw_grid(grid):
    # Initialize the number of stars needed to draw the grid
    num_stars = 0
    
    # Iterate through the grid and check if each cell is a center of a star
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '*':
                # Check if the cell is a center of a star of size 1
                if is_star(grid, row, col, 1):
                    num_stars += 1
                    print(f"{row} {col} 1")
                # Check if the cell is a center of a star of size 2
                elif is_star(grid, row, col, 2):
                    num_stars += 1
                    print(f"{row} {col} 2")
                # Check if the cell is a center of a star of size 3
                elif is_star(grid, row, col, 3):
                    num_stars += 1
                    print(f"{row} {col} 3")
    
    # If no stars are found, return -1
    if num_stars == 0:
        print(-1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]
    draw_grid(grid)

