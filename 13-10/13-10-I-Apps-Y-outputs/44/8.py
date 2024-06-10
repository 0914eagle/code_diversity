
def get_max_removable_substring(s, t):
    n = len(s)
    m = len(t)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s[i-1] == t[j-1]:
                dp[i][j] = max(dp[i-1][j-1] + 1, dp[i-1][j])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return m - dp[n][m]

def main():
    s = input()
    t = input()
    print(get_max_removable_substring(s, t))

if __name__ == '__main__':
    main()

