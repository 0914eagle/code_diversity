
def solve(s, k):
    n = len(s)
    if k > n:
        return -1
    
    # Initialize the dp table with the number of characters to change
    dp = [n] * (n + 1)
    
    # Loop through the characters of the string
    for i in range(n):
        # If the current character is 'R', 'G' or 'B', set the dp value to the minimum of the current value and the value at the previous index plus 1
        if s[i] in ["R", "G", "B"]:
            dp[i + 1] = min(dp[i], dp[i - 1] + 1)
    
    # Return the minimum number of characters to change
    return dp[n]

