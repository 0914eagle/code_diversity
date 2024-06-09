
def count_regular_sequences(n, s):
    MOD = 10**9 + 7
    m = len(s)
    dp = [[0] * (m + 1) for _ in range(m + 1)]
    dp[0][0] = 1

    for i in range(1, m + 1):
        for j in range(m + 1):
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]
            if j < m:
                dp[i][j] += dp[i - 1][j + 1]
            dp[i][j] %= MOD

    left = s.count('(')
    right = s.count(')')
    balance = 0
    for c in s:
        if c == '(':
            balance += 1
        else:
            balance -= 1

    result = 0
    for i in range(n - m + 1):
        if balance + i >= 0 and balance + i <= n - m:
            result += dp[n - m][balance + i]
            result %= MOD

    return result

n = int(input())
s = input()
print(count_regular_sequences(n, s))
