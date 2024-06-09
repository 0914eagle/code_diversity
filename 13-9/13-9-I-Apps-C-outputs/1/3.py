
def solve(n, m, grid):
    # Initialize the number of north and south magnets
    north_magnets, south_magnets = 0, 0
    
    # Loop through each row and column
    for i in range(n):
        for j in range(m):
            # Check if the current cell is black
            if grid[i][j] == "#":
                # Check if there is a south magnet in the current row
                if any(grid[i][j+1:] == "."):
                    south_magnets += 1
                # Check if there is a south magnet in the current column
                if any(grid[i+1:, j] == "."):
                    south_magnets += 1
    
    # Check if there is at least one south magnet in each row and column
    if south_magnets < n or south_magnets < m:
        return -1
    
    # Loop through each row and column
    for i in range(n):
        for j in range(m):
            # Check if the current cell is white
            if grid[i][j] == ".":
                # Check if there is a north magnet in the current row
                if any(grid[i][:j] == "#"):
                    north_magnets += 1
                # Check if there is a north magnet in the current column
                if any(grid[:i, j] == "#"):
                    north_magnets += 1
    
    # Return the minimum number of north magnets required
    return north_magnets

