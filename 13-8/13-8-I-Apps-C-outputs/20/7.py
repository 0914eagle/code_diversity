
def get_drained_water(grid, i, j):
    # Initialize the total drained water to 0
    total_drained_water = 0

    # Loop through the grid and find all the cells that are connected to the draining device
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] < 0 and (row, col) != (i, j):
                # If the cell is connected to the draining device, mark it as visited and add its water volume to the total
                total_drained_water += abs(grid[row][col])
                grid[row][col] = 0

                # Recursively visit all the neighbors of the current cell and mark them as visited if they are connected to the draining device
                for neighbor in get_neighbors(grid, row, col):
                    if grid[neighbor[0]][neighbor[1]] < 0 and (neighbor[0], neighbor[1]) != (i, j):
                        total_drained_water += abs(grid[neighbor[0]][neighbor[1]])
                        grid[neighbor[0]][neighbor[1]] = 0

    # Return the total drained water
    return total_drained_water

def get_neighbors(grid, row, col):
    # Get the neighbors of the current cell
    neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1),
                 (row-1, col-1), (row-1, col+1), (row+1, col-1), (row+1, col+1)]

    # Filter out the neighbors that are out of bounds or not connected to the draining device
    neighbors = [neighbor for neighbor in neighbors if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] < 0]

    return neighbors

def solve(grid, i, j):
    return get_drained_water(grid, i, j)

