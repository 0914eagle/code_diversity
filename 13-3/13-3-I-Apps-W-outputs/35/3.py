
import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = [list(map(int, input().split())) for _ in range(m)]

# Initialize the dp array with the initial values
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = max(dp[i - 1], a[i - 1] + dp[i - 1])

# Perform the operations
for j in range(m):
    for i in range(n, b[j][0] - 1, -1):
        dp[i] = max(dp[i], dp[i - b[j][0]] + b[j][1])

# Print the maximum sum
print(dp[n])

