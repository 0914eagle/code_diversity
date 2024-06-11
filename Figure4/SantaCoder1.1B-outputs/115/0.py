def max_fill(grid, capacity):
    import math
    
    rows = len(grid)
    cols = len(grid[0])
    bucket_capacity = capacity
    max_fill = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                bucket_capacity -= 1
                if bucket_capacity == 0:
                    max_fill += 1
                    bucket_capacity = capacity
    return max_fill

