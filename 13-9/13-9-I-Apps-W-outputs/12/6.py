
import sys

MOD = 1000000007

def count_paths(n, k, d):
    # Initialize the dp table with all values as 0
    dp = [0] * (n + 1)
    dp[0] = 1

    # Populate the dp table
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i - j >= 0:
                dp[i] += dp[i - j]

    # Return the result modulo MOD
    return dp[n] % MOD

n, k, d = map(int, input().split())
print(count_paths(n, k, d))

