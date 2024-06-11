

def minPath(grid, k):
    
    # Initialize the distance array with infinite distance
    distance = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
    # Initialize the previous array with -1
    previous = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Set the distance of the starting cell to 0
    distance[0][0] = 0
    previous[0][0] = -1

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is not the starting cell
            if i > 0 or j > 0:
                # Get the distances of the neighboring cells
                left_distance = distance[i][j - 1] if j > 0 else float('inf')
                right_distance = distance[i][j + 1] if j < len(grid[0]) - 1 else float('inf')
                top_distance = distance[i - 1][j] if i > 0 else float('inf')
                bottom_distance = distance[i + 1][j] if i < len(grid) - 1 else float('inf')

                # Calculate the minimum distance to the current cell
                min_distance = min(left_distance, right_distance, top_distance, bottom_distance) + 1

                # If the minimum distance is less than the current distance
                if min_distance < distance[i][j]:
                    # Update the distance and previous arrays
                    distance[i][j] = min_distance
                    previous[i][j] = (i, j)

    # Find the path that has the minimum distance
    min_distance = float('inf')
    path = []
    current_cell = (len(grid) - 1, len(grid[0]) - 1)
    while current_cell != (-1, -1):
        min_distance = min(min_distance, distance[current_cell[0]][current_cell[1]])
        path.append(grid[current_cell[0]][current_cell
