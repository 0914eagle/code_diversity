def max_fill(grid, capacity):
    import math
    
    m, n = len(grid), len(grid[0])
    # dp[i][j] := number of times to fill the jth bucket
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[i][j] = 1
                continue
            if i > 0 and grid[i-1][j] == 1:
                dp[i][j] += dp[i-1][j]
            if i < m-1 and grid[i+1][j] == 1:
                dp[i][j] += dp[i+1][j]
            if j > 0 and grid[i][j-1] == 1:
                dp[i][j] += dp[i][j-1]
            if j < n-1 and grid[i][j+1] == 1:
                dp[i][j] += dp[i][j+1]
    return sum(dp[i][j] for i in range(m) for j in range(n) if dp[i][j] < capacity)


if __name__ == "__main__":
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    bucket_capacity = 1
    print(max_fill(grid, bucket_capacity))

    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    bucket_capacity = 2
    print(max_fill(grid, bucket_capacity))

    grid = [[0,0,0], [0,0,0]]
    bucket_capacity = 5
    print(max_fill(grid, bucket_capacity))

    grid = [[0,0,0]]
    bucket_capacity = 5
    print(max_fill(grid, bucket_capacity))