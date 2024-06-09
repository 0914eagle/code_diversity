
def solve(n, m, grid):
    # Initialize the number of north and south magnets
    north_magnets = 0
    south_magnets = 0
    
    # Iterate over each row and column
    for i in range(n):
        for j in range(m):
            # Check if the current cell is black
            if grid[i][j] == "#":
                # If the current cell is black, we can place a north magnet here
                north_magnets += 1
            else:
                # If the current cell is white, we need to place a south magnet here
                south_magnets += 1
    
    # Check if it is possible to place the magnets such that all conditions are met
    if north_magnets >= south_magnets:
        return north_magnets
    else:
        return -1

