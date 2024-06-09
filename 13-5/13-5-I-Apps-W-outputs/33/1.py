
def get_max_score(values):
    n = len(values)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i + 1][j] + values[i])
    return dp[0][n]

def get_optimal_segment(values):
    n = len(values)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i + 1][j] + values[i])
            if dp[i][j] == dp[i][j - 1]:
                dp[i][j] = j - 1
            else:
                dp[i][j] = i
    return dp[0][n]

def main():
    n = int(input())
    values = list(map(int, input().split()))
    print(get_max_score(values))
    print(get_optimal_segment(values))

if __name__ == '__main__':
    main()

