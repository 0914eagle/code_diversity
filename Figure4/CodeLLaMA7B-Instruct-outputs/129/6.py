

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
                # Get the distances and previouses of the neighboring cells
                top = distance[i - 1][j]
                left = distance[i][j - 1]

                # Calculate the distance and previous for the current cell
                distance[i][j] = min(top, left) + 1
                previous[i][j] = top if top < left else left

    # Initialize the path with the starting cell
    path = [1]

    # Loop until the distance of the ending cell is reached
    while distance[len(grid) - 1][len(grid[0]) - 1] != k:
        # Get the previous cell of the ending cell
        cell = previous[len(grid) - 1][len(grid[0]) - 1]

        # Add the value of the previous cell to the path
        path.append(grid[len(grid) - 1][len(grid[0]) - 1])

        # Update the distance and previous of the previous cell
        distance[len(grid) - 1][len(grid[0]) - 1] = k
        previous[len(grid) - 1][len(grid[0]) - 1] = cell

    # Return the path in reverse order
    return path[::-1]


