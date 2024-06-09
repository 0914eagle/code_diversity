
def get_maximum_happiness(n, m, types):
    # Initialize the dp array with 0
    dp = [0] * (n + 1)

    # Loop through each type of flower
    for i in range(m):
        # Get the happiness for the current type
        a, b = types[i]

        # Loop through the number of flowers of the current type
        for j in range(1, n + 1):
            # Calculate the maximum happiness for the current number of flowers
            dp[j] = max(dp[j], dp[j - 1] + a + (j - 1) * b)

    # Return the maximum happiness
    return dp[n]

