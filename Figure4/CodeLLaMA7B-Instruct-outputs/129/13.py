

def minPath(grid, k):
    
    # Initialize the distance array with infinite distance
    distance = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Initialize the previous array with -1
    previous = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Initialize the distance and previous for the starting cell
    distance[0][0] = 0
    previous[0][0] = -1

    # Loop through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is not the starting cell
            if i > 0 or j > 0:
                # Get the distances and previous for the current cell
                current_distance = distance[i][j]
                current_previous = previous[i][j]

                # Loop through the neighboring cells
                for neighbor_i in range(max(0, i - 1), min(len(grid), i + 2)):
                    for neighbor_j in range(max(0, j - 1), min(len(grid[0]), j + 2)):
                        # If the neighboring cell is not the current cell
                        if neighbor_i != i or neighbor_j != j:
                            # Get the distance and previous for the neighboring cell
                            neighbor_distance = distance[neighbor_i][neighbor_j]
                            neighbor_previous = previous[neighbor_i][neighbor_j]

                            # If the neighboring cell is not visited yet or the current cell is closer
                            if neighbor_distance == float('inf') or current_distance + grid[i][j] < neighbor_distance:
                                # Update the distance and previous for the neighboring cell
                                distance[neighbor_i][neighbor_j] = current_distance + grid[i][j]
                                previous[neighbor_i][neighbor_j] = i * len(grid[0]) + j

    # Find the minimum distance and previous for the ending cell
    minimum_distance = float('inf')
    minimum_previous =
