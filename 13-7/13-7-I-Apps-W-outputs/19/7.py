
def get_max_cost(s, p):
    n = len(s)
    if n == 0 or p == 0:
        return 0

    # Convert the string to a list of characters
    chars = list(s)

    # Initialize the dp table with 0s
    dp = [0] * (n + 1)

    # Loop through each character in the string
    for i in range(1, n + 1):
        # If the current character is different from the previous character
        if chars[i - 1] != chars[i - 2]:
            # Set the current value to the previous value plus 1
            dp[i] = dp[i - 1] + 1
        else:
            # Set the current value to the maximum of the previous value and the previous previous value plus 1
            dp[i] = max(dp[i - 1], dp[i - 2] + 1)

    # Return the maximum value in the dp table
    return max(dp)

