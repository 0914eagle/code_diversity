

def minPath(grid, k):
    
    # Initialize a dictionary to store the minimum path and its length
    min_path = {}
    # Initialize a dictionary to store the previous cell for each cell
    previous_cell = {}

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # If the cell is not visited yet, add it to the queue
            if grid[i][j] not in min_path:
                min_path[grid[i][j]] = [i, j]
                previous_cell[grid[i][j]] = None

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # If the cell is not visited yet, add it to the queue
            if grid[i][j] not in min_path:
                min_path[grid[i][j]] = [i, j]
                previous_cell[grid[i][j]] = None

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # If the cell is not visited yet, add it to the queue
            if grid[i][j] not in min_path:
                min_path[grid[i][j]] = [i, j]
                previous_cell[grid[i][j]] = None

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # If the cell is not visited yet, add it to the queue
            if grid[i][j] not in min_path:
                min_path[grid[i][j]] = [i, j]
                previous_cell[grid[i][j]] = None

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # If the cell is not visited yet, add it to the queue
            if grid[i][j] not in min_path:
                min_path[grid[
