
def solve(n, m, grid):
    # Initialize the number of north and south magnets
    north_magnets, south_magnets = 0, 0
    
    # Loop through each row and column
    for i in range(n):
        for j in range(m):
            # Check if the current cell is black
            if grid[i][j] == "#":
                # If the current cell is black, check if there is a south magnet in the same row or column
                if any(grid[i][k] == "." for k in range(m)) or any(grid[k][j] == "." for k in range(n)):
                    # If there is a south magnet in the same row or column, increase the number of north magnets
                    north_magnets += 1
                else:
                    # If there is no south magnet in the same row or column, return -1
                    return -1
            else:
                # If the current cell is white, check if there is a north magnet in the same row or column
                if any(grid[i][k] == "#" for k in range(m)) or any(grid[k][j] == "#" for k in range(n)):
                    # If there is a north magnet in the same row or column, return -1
                    return -1
                else:
                    # If there is no north magnet in the same row or column, increase the number of south magnets
                    south_magnets += 1
    
    # Return the minimum number of north magnets required
    return north_magnets

