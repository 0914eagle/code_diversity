
def get_path_count(grid, k):
    n, m = len(grid), len(grid[0])
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            dp[i][j] += dp[i - 1][j]
            if j > 1 and grid[i - 1][j - 2] ^ grid[i - 1][j - 1] == k:
                dp[i][j] += dp[i - 1][j - 1]
            if i > 1 and grid[i - 2][j - 1] ^ grid[i - 1][j - 1] == k:
                dp[i][j] += dp[i - 1][j - 1]
    return dp[n][m]

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(get_path_count(grid, k))

if __name__ == '__main__':
    main()

