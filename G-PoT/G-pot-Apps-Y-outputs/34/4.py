
n, k, x = map(int, input().split())
beauty_values = list(map(int, input().split()))

dp = [[-1] * (x + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(1, x + 1):
        for l in range(max(0, i - k), i):
            if dp[l][j - 1] != -1:
                dp[i][j] = max(dp[i][j], dp[l][j - 1] + beauty_values[i - 1])

result = max(dp[n])
if result == 0:
    print(-1)
else:
    print(result)
