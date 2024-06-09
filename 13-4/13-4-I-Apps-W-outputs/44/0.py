
def solve(s):
    n = len(s)
    # Initialize the dp table with the length of the longest non-decreasing subsequence of the first character
    dp = [1] * n
    # Initialize the previous index table with -1
    prev = [-1] * n
    # Loop through the string
    for i in range(1, n):
        # If the current character is 1, set the length of the longest non-decreasing subsequence to 1
        if s[i] == "1":
            dp[i] = 1
        # Otherwise, find the maximum length of the longest non-decreasing subsequence by comparing the length of the longest non-decreasing subsequence of the previous character with the length of the longest non-decreasing subsequence of the current character
        else:
            dp[i] = max(dp[i-1], 1)
            prev[i] = i-1
    # Find the maximum length of the longest non-decreasing subsequence
    max_len = max(dp)
    # Initialize the result string with the first character
    result = s[0]
    # Loop through the string
    for i in range(1, n):
        # If the length of the longest non-decreasing subsequence is equal to the maximum length, add the current character to the result string
        if dp[i] == max_len:
            result += s[i]
    return result

