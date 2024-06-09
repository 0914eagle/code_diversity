
import sys

def k_tree_paths(n, k, d):
    mod = 1000000007
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 1
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            if j >= d:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i][j - 1]) % mod
            else:
                dp[i][j] = dp[i][j - 1]
    return dp[k][n]

n, k, d = map(int, sys.stdin.readline().strip().split())
print(k_tree_paths(n, k, d))

