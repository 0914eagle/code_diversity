def max_fill(grid, capacity):
    import math
    
    # 1. 记录每个格子的最大容量
    max_capacity = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                max_capacity = max(max_capacity, grid[i][j])
    # 2. 记录每个格子的最大容量
    max_capacity = max(max_capacity, capacity)
    # 3. 记录每个格子的最大容量
    max_capacity = max(max_capacity, capacity * len(grid))
    # 4. 记录每个格子的最大容量
    max_capacity = max(max_capacity, capacity * len(grid[0]))
    # 5. 记录每个格子的最大容量
    max_capacity = max(max_capacity, capacity * len(grid) * len(grid[0]))
    # 6. 记录每个格子的最大容量
    max_capacity = max(max_capacity, capacity * len(grid) * len(grid[0]) * len(grid[0]))
    # 7. 记录每个格子的最大容量
    max_capacity = max(max_capacity, capacity * len(grid) * len(grid[0]) * len(grid[0]) * len(grid[0]))
    # 8. 记录每个格子的最大容量
    max_capacity = max(max_capacity, capacity * len(grid) * len(grid[0]) * len(grid[0]) * len(grid[0]) * len(grid[0]))
    # 9. 记录每个格子的最大容量
    max_capacity = max(max_capacity, capacity * len(grid) * len(grid[0]) * len(grid[0]) * len(grid[0]) * len(grid[0]) * len(grid[0]))
    # 10. 记录每个格子的最大容量
    max_capacity = max(max_capacity, capacity * len(grid) * len(grid[0]) * len(grid[0]) * len(grid[0]) * len(grid[0]) * len(grid[0]) * len(grid[0]))
    # 11. 记录每个格子的最大容量