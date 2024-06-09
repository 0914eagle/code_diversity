
def solve(s):
    n = len(s)
    # Initialize the longest non-decreasing subsequence for each prefix of the string
    longest_non_decreasing_subsequence = [1] * (n + 1)
    # Initialize the previous index for each prefix of the string
    previous_index = [0] * (n + 1)
    
    # Loop through each prefix of the string
    for i in range(1, n + 1):
        # Loop through each prefix of length i
        for j in range(1, i + 1):
            # If the current character is 0 and the previous character is 1, update the longest non-decreasing subsequence and the previous index
            if s[i - j] == "0" and s[i - j - 1] == "1":
                longest_non_decreasing_subsequence[i] = max(longest_non_decreasing_subsequence[i], longest_non_decreasing_subsequence[i - j] + 1)
                previous_index[i] = j
    
    # Initialize the binary string t with all 0s
    t = "0" * n
    
    # Loop through each suffix of the string
    for i in range(n - 1, -1, -1):
        # If the current character is 1 and the previous character is 0, update the binary string t
        if s[i] == "1" and s[i - 1] == "0":
            t = t[:i] + "1" + t[i + 1:]
    
    return t

