
import sys

mod = 1000000007

def num_paths(n, k, d):
    # Initialize the dp table with 0s
    dp = [0] * (n + 1)
    dp[0] = 1
    
    # Iterate over the values of n
    for i in range(1, n + 1):
        # Iterate over the values of k
        for j in range(1, k + 1):
            # If j is greater than or equal to d, add the number of paths from the previous value of n and k
            if j >= d:
                dp[i] = (dp[i] + dp[i - 1]) % mod
    
    return dp[n]

n, k, d = map(int, input().split())
print(num_paths(n, k, d))

