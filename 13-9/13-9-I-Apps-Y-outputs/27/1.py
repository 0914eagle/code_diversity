
def find_paths(grid, k):
    n, m = len(grid), len(grid[0])
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[n][m] = 1
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            dp[i][j] = dp[i+1][j] + dp[i][j+1]
            if grid[i][j] ^ k == 0:
                dp[i][j] += dp[i+1][j+1]
    return dp[0][0]

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(find_paths(grid, k))

if __name__ == '__main__':
    main()

