
def count_ways(n, m, a):
    # Initialize a table to store the results
    dp = [0] * (n+1)
    dp[0] = 1

    # Iterate over the broken steps
    for i in range(m):
        # Iterate over the possible steps to reach the broken step
        for j in range(a[i]):
            # If the step is not broken, add the number of ways to reach it
            if j not in a:
                dp[j+1] += dp[j]

    # Return the number of ways to reach the top step
    return dp[n] % 1000000007

