
def solve(n, m, grid):
    # Initialize the number of north and south magnets
    num_north, num_south = 0, 0
    
    # Loop through each row and column
    for i in range(n):
        for j in range(m):
            # Check if the current cell is black
            if grid[i][j] == "#":
                # Check if there is a south magnet in the same row
                if any(grid[i][k] == "." for k in range(m)):
                    num_south += 1
                # Check if there is a south magnet in the same column
                if any(grid[k][j] == "." for k in range(n)):
                    num_south += 1
    
    # Check if there are enough south magnets
    if num_south < n + m:
        return -1
    
    # Loop through each row and column
    for i in range(n):
        for j in range(m):
            # Check if the current cell is white
            if grid[i][j] == ".":
                # Check if there is a north magnet in the same row
                if any(grid[i][k] == "#" for k in range(m)):
                    num_north += 1
                # Check if there is a north magnet in the same column
                if any(grid[k][j] == "#" for k in range(n)):
                    num_north += 1
    
    # Return the minimum number of north magnets required
    return num_north

