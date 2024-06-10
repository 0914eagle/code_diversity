
def get_subset(x):
    n = len(x)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = 1
            elif x[i - 1] - x[j - 1] == 2 ** dp[i - 1][j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][n]

def get_subset_coords(x, y):
    n = len(x)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = [x[i - 1]]
            elif x[i - 1] - x[j - 1] == 2 ** dp[i - 1][j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + [x[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]
    return dp[n][n]

def main():
    n = int(input())
    x = list(map(int, input().split()))
    y = get_subset_coords(x, n)
    print(len(y))
    print(*y)

if __name__ == '__main__':
    main()

