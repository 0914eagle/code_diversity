def minPath(grid, k):
    
    # get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])
    # create a visited matrix
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    # create a matrix to store the minimum path to each cell
    min_path = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    # create a matrix to store the path to each cell
    path = [[[] for _ in range(cols)] for _ in range(rows)]
    # initialize the top row
    for col in range(cols):
        min_path[0][col] = grid[0][col]
        path[0][col] = [grid[0][col]]
    # initialize the left column
    for row in range(rows):
        min_path[row][0] = grid[row][0]
        path[row][0] = [grid[row][0]]
    # iterate through the grid
    for row in range(1, rows):
        for col in range(1, cols):
            # if the cell has not been visited
            if not visited[row][col]:
                # get the minimum path to the cell above
                min_path_above = min_path[row-1][col]
                # get the minimum path to the cell to the left
                min_path_left = min_path[row][col-1]
                # get the minimum path to the cell to the left and above
                min_path_left_and_above = min_path[row-1][col-1]
                # get the minimum path to the cell
                min_path[row][col] = min(min_path_above, min_path_left, min_path_left_and_above) + grid[row][col]
                # get the path to the cell
                path[row][col] = path[row-1][col] if min_path_above <= min_path_left and min_path_above <= min_path_left_and_above else path[row][col-1] if min_path_left <= min_path_above and min_path_left <= min_path_left_