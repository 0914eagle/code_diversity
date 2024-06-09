
def solve(n, m, grid):
    # Initialize the number of north and south magnets
    num_north, num_south = 0, 0
    
    # Loop through each row and column
    for i in range(n):
        for j in range(m):
            # If the current cell is black, we need to find a way to place a north magnet in this cell
            if grid[i][j] == '#':
                # If the cell is in the first row or column, we can place a north magnet in this cell
                if i == 0 or j == 0:
                    num_north += 1
                # If the cell is in the last row or column, we can place a north magnet in this cell
                elif i == n-1 or j == m-1:
                    num_north += 1
                # If the cell is in the middle of the grid, we need to find a way to move a north magnet to this cell
                else:
                    # Initialize the minimum number of north magnets required to move a north magnet to this cell
                    min_north = float('inf')
                    # Loop through each cell in the same row as the current cell
                    for k in range(m):
                        # If the current cell is black and there is a north magnet in the cell to the left of the current cell, we can move the north magnet to the current cell
                        if grid[i][k] == '#' and grid[i][k-1] == 'N':
                            min_north = min(min_north, num_north-1)
                        # If the current cell is black and there is a north magnet in the cell to the right of the current cell, we can move the north magnet to the current cell
                        if grid[i][k] == '#' and grid[i][k+1] == 'N':
                            min_north = min(min_north, num_north-1)
                    # Loop through each cell in the same column as the current cell
                    for k in range(n):
                        # If the current cell is black and there is a north magnet in the cell above the current cell, we can move the north magnet to the current cell
                        if grid[k][j] == '#' and grid[k-1][j] == 'N':
                            min_north = min(min_north, num_north-1)
                        # If the current cell is black and there is a north magnet in the cell below the current cell, we can move the north magnet to the current cell
                        if grid[k][j] == '#' and grid[k+1][j] == 'N':
                            min_north = min(min_north, num_north-1)
                    # If we cannot move a north magnet to this cell, return -1
                    if min_north == float('inf'):
                        return -1
                    # Otherwise, update the number of north magnets required
                    num_north += min_north
    
    # Return the number of north magnets required
    return num_north

