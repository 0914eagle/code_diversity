
import math

def solve(n, arr):
    # Calculate the number of factors for each number
    factors = [0] * (n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors[i] = 1
            if i * i != n:
                factors[n // i] = 1

    # Initialize the dp table with the number of ways to form a path with no streamers
    dp = [1] * (n + 1)

    # Iterate through the array and calculate the number of ways to form a path with streamers
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and factors[arr[i - 1]] and factors[arr[j - 1]]:
                dp[i] = (dp[i] + dp[j]) % 1000000007

    return dp[n]

