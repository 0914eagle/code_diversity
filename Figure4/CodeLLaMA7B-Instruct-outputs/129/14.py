

def minPath(grid, k):
    
    # Initialize the distance array with infinite distance
    distance = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Initialize the previous array with -1
    previous = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Initialize the queue with the starting cell
    queue = [(0, 0)]

    # Loop until the queue is empty
    while queue:
        # Get the current cell from the queue
        x, y = queue.pop(0)

        # If the current cell is the destination cell, return the path
        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            path = []
            while x != 0 or y != 0:
                path.append(grid[x][y])
                x, y = previous[x][y]
            path.reverse()
            return path

        # Loop through all the neighboring cells
        for i in range(max(x - 1, 0), min(x + 2, len(grid))):
            for j in range(max(y - 1, 0), min(y + 2, len(grid[0]))):
                # If the neighboring cell is not the starting cell and the distance is not infinite
                if i != x or j != y:
                    # Calculate the distance to the neighboring cell
                    distance_to_neighbor = grid[i][j] + distance[x][y]

                    # If the distance is less than the current distance, update the distance and previous arrays
                    if distance_to_neighbor < distance[i][j]:
                        distance[i][j] = distance_to_neighbor
                        previous[i][j] = (x, y)

        # Add the current cell to the queue
        queue.append((x, y))

    # If the destination cell is not found, return -1
    return -1


