
def solve(n, m, grid):
    # Initialize the number of north and south magnets
    north_magnets = 0
    south_magnets = 0
    
    # Loop through each row and column
    for i in range(n):
        for j in range(m):
            # If the current cell is black, increment the number of north magnets
            if grid[i][j] == "."
                north_magnets += 1
            # If the current cell is white, increment the number of south magnets
            elif grid[i][j] == "#"
                south_magnets += 1
    
    # Return the minimum number of north magnets required
    return north_magnets

