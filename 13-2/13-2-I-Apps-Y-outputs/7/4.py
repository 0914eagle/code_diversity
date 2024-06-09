
def count_ways(n, m, a):
    # Initialize a table to store the results
    dp = [0] * (n+1)
    dp[0] = 1

    # Iterate over the broken steps
    for i in range(m):
        # Iterate over the remaining steps
        for j in range(a[i]-1, n):
            # Add the previous result to the current result
            dp[j+1] += dp[j]

    # Return the result modulo 1000000007
    return dp[n] % 1000000007

