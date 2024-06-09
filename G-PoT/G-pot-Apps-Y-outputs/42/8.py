
def count_regular_sequences(n, s):
    MOD = 1000000007
    m = len(s)
    dp = [[0] * (m + 1) for _ in range(m + 1)]
    dp[0][0] = 1

    for i in range(1, m + 1):
        for j in range(m + 1):
            if s[i - 1] == '(':
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD
            else:
                dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % MOD
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD

    total = dp[m][0]
    for i in range(m + 1, n * 2 + 1):
        total = (total * i) % MOD

    return total

n = int(input())
s = input()
result = count_regular_sequences(n, s)
print(result)
