
MOD = 10**9 + 7

n, m = map(int, input().split())
hints = []
for _ in range(m):
    l, r, hint = input().split()
    hints.append((int(l), int(r), hint))

dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1

for length in range(2, n+1):
    for i in range(n-length+1):
        j = i + length - 1
        for l, r, hint in hints:
            if i+1 <= l <= r+1 <= j+1:
                if hint == 'same':
                    dp[i][j] = (dp[i][j] + dp[i][l-2] * dp[r][j]) % MOD
                else:
                    dp[i][j] = (dp[i][j] + (dp[i][l-2] + dp[l-1][r-2] + dp[r-1][j]) * dp[r][j]) % MOD

print(dp[0][n-1])
