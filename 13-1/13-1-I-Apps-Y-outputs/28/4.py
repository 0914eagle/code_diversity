
def get_min_cost(s, k):
    n = len(s)
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i-1][j-1] + 1, dp[i-1][j] + 1, dp[i][j-1] + 1)
    return dp[n][k]

def main():
    n, k = map(int, input().split())
    s = input()
    print(get_min_cost(s, k))

if __name__ == '__main__':
    main()

