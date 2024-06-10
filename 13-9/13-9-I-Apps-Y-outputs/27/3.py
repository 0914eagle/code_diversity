
def get_number_of_paths(grid, k):
    n, m = len(grid), len(grid[0])
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[n][m] = 1
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            dp[i][j] += dp[i+1][j]
            if j < m-1 and grid[i][j] ^ grid[i][j+1] == k:
                dp[i][j] += dp[i][j+1]
            if i < n-1 and grid[i][j] ^ grid[i+1][j] == k:
                dp[i][j] += dp[i+1][j]
    return dp[0][0]

def main():
    n, m, k = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))
    print(get_number_of_paths(grid, k))

if __name__ == '__main__':
    main()

