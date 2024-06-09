
def solve(n, m, grid):
    # Initialize the number of north and south magnets
    north_magnets, south_magnets = 0, 0
    
    # Loop through each row and column
    for i in range(n):
        for j in range(m):
            # Check if the current cell is black
            if grid[i][j] == "B":
                # Check if there is a south magnet in the current row
                if not any(grid[i][k] == "S" for k in range(m)):
                    return -1
                # Check if there is a south magnet in the current column
                if not any(grid[k][j] == "S" for k in range(n)):
                    return -1
    
    # Loop through each row and column
    for i in range(n):
        for j in range(m):
            # Check if the current cell is black
            if grid[i][j] == "B":
                # Check if there is a north magnet in the current row
                if any(grid[i][k] == "N" for k in range(m)):
                    north_magnets += 1
                # Check if there is a north magnet in the current column
                if any(grid[k][j] == "N" for k in range(n)):
                    north_magnets += 1
    
    # Return the minimum number of north magnets required
    return north_magnets

