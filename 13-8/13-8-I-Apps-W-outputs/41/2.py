
def get_maximum_happiness(n, m, types):
    # Initialize the dp table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Loop through each type of flower
    for i in range(1, m + 1):
        # Get the amount of happiness and cost for the current type
        happiness, cost = types[i - 1]

        # Loop through each amount of flowers of the current type
        for j in range(1, n + 1):
            # If the current type is the first type, set the happiness to the amount of happiness
            if i == 1:
                dp[i][j] = happiness * j
            # If the current type is not the first type, calculate the maximum happiness by comparing the current type with the previous types
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + happiness * j)

    # Return the maximum happiness for the last type
    return dp[m][n]

