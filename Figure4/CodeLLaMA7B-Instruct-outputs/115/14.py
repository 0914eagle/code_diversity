

def max_fill(grid, capacity):
    import math
    
    # Initialize variables
    n_rows = len(grid)
    n_cols = len(grid[0])
    max_water = 0
    total_water = 0
    rows_to_fill = []
    cols_to_fill = []
    rows_to_empty = []
    cols_to_empty = []

    # Find the maximum amount of water in the grid
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == 1:
                max_water += 1

    # Find the rows and columns that need to be filled
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == 1:
                rows_to_fill.append(i)
                cols_to_fill.append(j)

    # Find the rows and columns that need to be emptied
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == 0:
                rows_to_empty.append(i)
                cols_to_empty.append(j)

    # Fill the rows and columns
    for i in range(len(rows_to_fill)):
        for j in range(len(cols_to_fill)):
            if rows_to_fill[i] == cols_to_fill[j]:
                total_water += 1
                if total_water > capacity:
                    total_water = capacity
                    break

    # Empty the rows and columns
    for i in range(len(rows_to_empty)):
        for j in range(len(cols_to_empty)):
            if rows_to_empty[i] == cols_to_empty[j]:
                total_water -= 1
                if total_water < 0:
                    total_water = 0
                    break

    # Return the number of times the buckets need to be lowered
    return math.ceil(total_water / capacity)

# Test case 1:
grid = [[0,0,1,0],
