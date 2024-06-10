
def get_max_substring_length(s, t):
    n = len(s)
    m = len(t)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = max(dp[i-1][j-1] + 1, dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return m - dp[n][m]

def main():
    s = input()
    t = input()
    print(get_max_substring_length(s, t))

if __name__ == '__main__':
    main()

