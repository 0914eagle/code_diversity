
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
    
    # Iterate over the grid
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
    
    # If the number of stars exceeds the maximum allowed, return -1
    if num_stars > len(grid) * len(grid[0]):
        return "-1"
    
    # Otherwise, return the number of stars and their positions
    return str(num_stars) + "\n" + "\n".join([str(row + 1) + " " + str(col + 1) + " " + str(size) for row, col, size in stars])

def main():
    # Read the input grid
    grid = []
    for _ in range(int(input())):
        grid.append(list(input()))
    
    # Draw the grid
    print(draw_grid(grid))

if __name__ == "__main__":
    main()

