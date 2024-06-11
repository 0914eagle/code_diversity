def max_fill(grid, capacity):
    import math
    
    # 1. find the max row and col
    row, col = len(grid), len(grid[0])
    # 2. find the max water in each row
    max_water = [0] * row
    for i in range(row):
        max_water[i] = max(max_water[i], grid[i][0])
    # 3. find the max water in each col
    max_water = [0] * col
    for i in range(col):
        max_water[i] = max(max_water[i], grid[0][i])
    # 4. find the max water in each row and col
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                max_water[i] = max(max_water[i], max_water[j] + 1)
    # 5. find the max water in each row and col
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                max_water[i] = max(max_water[i], max_water[j] - 1)
    # 6. find the max water in each row and col
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                max_water[i] = max(max_water[i], max_water[j] + grid[i][j])
    # 7. find the max water in each row and col
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                max_water[i] = max(max_water[i], max_water[j] - grid[i][j])
    # 8. find the max water in each row and col
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                max_water[i] = max(max_water[i], max_water[j] + 1 + max_water[j + 1])
    # 9. find the max water in each row and col
    for i in range(row):
        for j in range