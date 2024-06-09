
def solve(s, t):
    # Initialize variables
    max_length = 0
    s_len = len(s)
    t_len = len(t)

    # Loop through all possible starting indices of t in s
    for i in range(s_len - t_len + 1):
        # Check if t is a subsequence of s starting from index i
        if s[i:i+t_len] == t:
            # If it is, update the maximum length
            max_length = max(max_length, t_len)

    # Return the maximum length
    return max_length

