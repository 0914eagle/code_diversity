

def max_fill(grid, capacity):
    import math
    
    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    bucket_count = 0
    total_water = 0

    # Loop through the grid and count the number of water units
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                total_water += 1

    # If the total water is less than or equal to the bucket capacity,
    # there is no need to use buckets
    if total_water <= capacity:
        return 0

    # Loop through the grid and find the first well with water
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                # Increment the bucket count and mark the well as visited
                bucket_count += 1
                visited[i][j] = True

                # Loop through the neighbors of the well and mark them as visited
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if 0 <= k < rows and 0 <= l < cols and grid[k][l] == 1 and not visited[k][l]:
                            visited[k][l] = True

    # Return the number of buckets needed
    return bucket_count

# Test case 1:
grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
capacity = 1
