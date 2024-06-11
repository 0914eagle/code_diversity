

def minPath(grid, k):
    
    # Initialize a dictionary to store the minimum path and its length
    min_path = {}
    min_path_length = float('inf')

    # Initialize a dictionary to store the visited cells
    visited = {}

    # Initialize a queue to store the cells to be visited
    queue = []

    # Add the starting cell to the queue and visited dictionary
    queue.append((0, 0))
    visited[(0, 0)] = 0

    # Loop until the queue is empty
    while queue:
        # Get the current cell from the queue
        cell = queue.pop(0)

        # If the current cell has the minimum path length, add it to the minimum path
        if visited[cell] == min_path_length:
            min_path[cell] = visited[cell]

        # Get the neighbors of the current cell
        neighbors = get_neighbors(grid, cell)

        # Loop through the neighbors
        for neighbor in neighbors:
            # If the neighbor has not been visited, mark it as visited and add it to the queue
            if neighbor not in visited:
                visited[neighbor] = visited[cell] + 1
                queue.append(neighbor)

    # Return the minimum path
    return min_path

def get_neighbors(grid, cell):
    
    # Get the row and column of the cell
    row, col = cell

    # Get the number of rows and columns in the grid
    num_rows, num_cols = len(grid), len(grid[0])

    # Get the neighbors
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if row < num_rows - 1:
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col < num_cols - 1:
        neighbors.append((row, col + 1))

    return neighbors


