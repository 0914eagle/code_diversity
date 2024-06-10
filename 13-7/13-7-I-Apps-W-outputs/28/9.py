
def get_correct_fields(s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            if s[j] == '*':
                dp[i][j] += dp[i - 1][j]
            elif s[j] == '?':
                dp[i][j] += dp[i - 1][j - 1]
            else:
                dp[i][j] += dp[i - 1][j - 1] + dp[i - 1][j]
    return dp[n][0] % 1000000007

def main():
    s = input()
    print(get_correct_fields(s))

if __name__ == '__main__':
    main()

