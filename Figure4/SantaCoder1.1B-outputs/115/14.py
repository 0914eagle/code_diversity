def max_fill(grid, capacity):
    import math
    
    # 1st solution
    # O(n^2) time | O(1) space
    # n = len(grid)
    # for i in range(n):
    #     for j in range(n):
    #         if grid[i][j] == 1:
    #             grid[i][j] = 0
    #             if i > 0 and grid[i-1][j] == 1:
    #                 grid[i-1][j] = 0
    #             if i < n-1 and grid[i+1][j] == 1:
    #                 grid[i+1][j] = 0
    #             if j > 0 and grid[i][j-1] == 1:
    #                 grid[i][j-1] = 0
    #             if j < n-1 and grid[i][j+1] == 1:
    #                 grid[i][j+1] = 0
    # return len(grid)

    # 2nd solution
    # O(n) time | O(1) space
    # n = len(grid)
    # for i in range(n):
    #     for j in range(n):
    #         if grid[i][j] == 1:
    #             grid[i][j] = 0
    #             if i > 0 and grid[i-1][j] == 1:
    #                 grid[i-1][j] = 0
    #             if i < n-1 and grid[i+1][j] == 1:
    #                 grid[i+1][j] = 0
    #             if j > 0 and grid[i][j-1] == 1:
    #                 grid[i][j-1] = 0
    #             if j < n-1 and grid[i][j+1] == 1:
    #                 grid[i][j+1] = 0
    # return 0

    # 3rd solution
    # O(n) time | O(1) space
    # n = len(grid)
    # for i in range(n):
    #     for j in range(n):
    #         if grid[i][j] == 1:
    #             grid[i][j] =