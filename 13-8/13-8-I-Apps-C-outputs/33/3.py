
def solve(n, m, grid):
    # Initialize the number of north and south magnets
    north_magnets, south_magnets = 0, 0
    
    # Iterate over each row and column
    for i in range(n):
        for j in range(m):
            # Check if the current cell is black
            if grid[i][j] == "#":
                # Increment the number of south magnets
                south_magnets += 1
            # Check if the current cell is white
            elif grid[i][j] == ".":
                # Increment the number of north magnets
                north_magnets += 1
    
    # Check if there is at least one south magnet in each row and column
    for i in range(n):
        for j in range(m):
            # Check if the current cell is black
            if grid[i][j] == "#":
                # Check if there is a south magnet in the current row
                if not any(grid[i][k] == "." for k in range(m)):
                    return -1
                # Check if there is a south magnet in the current column
                if not any(grid[k][j] == "." for k in range(n)):
                    return -1
    
    # Return the minimum number of north magnets required
    return north_magnets

