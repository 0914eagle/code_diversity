
def get_number_of_paths(grid, k):
    n, m = len(grid), len(grid[0])
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if i == n and j == m:
                continue
            if i < n and j < m:
                dp[i][j] += dp[i - 1][j] + dp[i][j - 1]
            elif i < n:
                dp[i][j] += dp[i - 1][j]
            elif j < m:
                dp[i][j] += dp[i][j - 1]
    return dp[n][m]

def get_xor_sum(grid):
    n, m = len(grid), len(grid[0])
    xor_sum = 0
    for i in range(n):
        for j in range(m):
            xor_sum ^= grid[i][j]
    return xor_sum

def get_paths_with_xor_sum(grid, k):
    number_of_paths = get_number_of_paths(grid, k)
    xor_sum = get_xor_sum(grid)
    if xor_sum == k:
        return number_of_paths
    else:
        return 0

if __name__ == '__main__':
    grid = [[2, 1, 5], [7, 10, 0], [12, 6, 4]]
    k = 11
    print(get_paths_with_xor_sum(grid, k))

