
def get_optimal_cut(s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i + 1][j] + 1)
            if s[i] != s[j - 1]:
                dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + 1)
    return dp[0][n]

def main():
    n = int(input())
    s = input()
    print(get_optimal_cut(s))

if __name__ == '__main__':
    main()

