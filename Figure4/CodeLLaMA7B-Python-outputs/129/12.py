def minPath(grid, k):
    
    # Time Complexity: O(N*N)
    # Space Complexity: O(N*N)
    # N = number of rows in grid
    # M = number of columns in grid
    # N <= M
    # grid: List[List[int]]
    # k: int
    # return: List[int]

    # if k == 1:
    #     return [min(grid[0])]

    # N = len(grid)
    # M = len(grid[0])

    # dp = [[[float('inf')] * (k + 1) for _ in range(M)] for _ in range(N)]
    # for i in range(N):
    #     for j in range(M):
    #         dp[i][j][1] = grid[i][j]

    # for i in range(1, k):
    #     for r in range(N):
    #         for c in range(M):
    #             if r > 0:
    #                 dp[r][c][i + 1] = min(dp[r][c][i + 1], dp[r - 1][c][i])
    #             if c > 0:
    #                 dp[r][c][i + 1] = min(dp[r][c][i + 1], dp[r][c - 1][i])
    #             if r < N - 1:
    #                 dp[r][c][i + 1] = min(dp[r][c][i + 1], dp[r + 1][c][i])
    #             if c < M - 1:
    #                 dp[r][c][i + 1] = min(dp[r][c][i + 1], dp[r][c + 1][i])

    # res = []
    # for i in range(k):
    #     res.append(dp[N - 1][M - 1][k])

    # return res

    if k == 1:
        return [min(grid[0])]

