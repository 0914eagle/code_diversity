
def solve(n, m, grid):
    # Initialize the number of north and south magnets
    north_magnets, south_magnets = 0, 0
    
    # Loop through each row and column
    for i in range(n):
        for j in range(m):
            # If the current cell is black, increase the number of north magnets
            if grid[i][j] == "." and north_magnets < 1:
                north_magnets += 1
            # If the current cell is white, increase the number of south magnets
            elif grid[i][j] == "#" and south_magnets < 1:
                south_magnets += 1
    
    # Return the minimum number of north magnets required
    return north_magnets

