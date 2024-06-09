
def count_ways(n, m, a):
    # Initialize a table to store the results
    dp = [0] * (n+1)
    dp[0] = 1

    # Iterate over the broken steps
    for i in range(m):
        # Iterate over the possible steps to reach the broken step
        for j in range(a[i]):
            # If the step is not already broken, add the number of ways to reach it
            if dp[j] > 0:
                dp[j] = (dp[j] + dp[j+1]) % 1000000007

    return dp[n]

