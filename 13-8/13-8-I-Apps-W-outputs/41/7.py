
def get_maximum_happiness(n, m, a, b):
    # Initialize the dp table with 0
    dp = [0] * (n + 1)

    # Loop through each type of flower
    for i in range(m):
        # Loop through each number of flowers
        for j in range(n + 1):
            # Check if the current number of flowers is greater than or equal to the number of flowers of the current type
            if j >= a[i]:
                # Update the dp table with the maximum of the current value and the previous value plus the happiness gained from the current type of flower
                dp[j] = max(dp[j], dp[j - a[i]] + b[i] * (j - a[i]))

    # Return the maximum total happiness
    return dp[n]

