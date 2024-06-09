
import math

def solve(n, arr):
    # Calculate the number of factors for each number
    factors = [0] * (n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors[i] += 1
            if i * i != n:
                factors[n // i] += 1

    # Initialize the dp table with the number of factors
    dp = [1] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = factors[i]

    # Calculate the number of ways to stretch the streamers
    for i in range(2, n + 1):
        for j in range(i + 1, n + 1):
            if arr[i - 1] % arr[j - 1] == 0 or arr[j - 1] % arr[i - 1] == 0:
                dp[j] = (dp[j] + dp[i]) % 1000000007

    return dp[n]

