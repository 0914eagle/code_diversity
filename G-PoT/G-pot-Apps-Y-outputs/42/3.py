
n = int(input())
s = input()

MOD = 10**9 + 7

def count_regular_sequences(n, s):
    m = len(s)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(m + 1):
            dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD
            if j < m and s[j] == '(':
                dp[i][j+1] = (dp[i][j+1] + dp[i-1][j]) % MOD

    return dp[n][m]

result = count_regular_sequences(n, s)
print(result)
