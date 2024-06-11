

def max_fill(grid, capacity):
    import math
    

    # Initialize variables
    m, n = len(grid), len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    bucket_count = 0
    total_water = 0

    # Loop through each row of the grid
    for i in range(m):
        # Loop through each column of the grid
        for j in range(n):
            # If the current cell is a water cell and not visited
            if grid[i][j] == 1 and not visited[i][j]:
                # Increment the bucket count
                bucket_count += 1
                # Set the current cell as visited
                visited[i][j] = True
                # Initialize the current cell as the starting cell
                start = (i, j)
                # Initialize the queue with the starting cell
                queue = [(start)]

                # Loop until the queue is empty
                while queue:
                    # Get the current cell from the queue
                    current = queue.pop(0)
                    # Get the row and column of the current cell
                    row, col = current
                    # If the current cell is not at the edge of the grid
                    if row > 0 and not visited[row - 1][col]:
                        # Add the cell above the current cell to the queue
                        queue.append((row - 1, col))
                        # Set the cell above the current cell as visited
                        visited[row - 1][col] = True
                    if row < m - 1 and not visited[row + 1][col]:
                        # Add the cell below the current cell to the queue
                        queue.append((row + 1, col))
                        # Set the cell below the current cell as visited
                        visited[row + 1][col] = True
                    if col > 0 and not visited[row][col - 1]:
                        # Add the cell to the left of the current cell to the queue
                        queue.append((row, col - 1))
                        # Set the cell to the left of the current cell as visited
                        visited[row][col - 1] = True
                    if col <
