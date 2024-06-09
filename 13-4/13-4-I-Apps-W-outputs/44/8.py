
def solve(s):
    n = len(s)
    # Initialize the longest non-decreasing subsequence of s and t to be of length 1
    longest_subsequence_s = [1] * n
    longest_subsequence_t = [1] * n
    # Initialize the number of zeroes in t to be 0
    num_zeroes = 0
    # Loop through the string s
    for i in range(1, n):
        # If the current character of s is 0
        if s[i] == "0":
            # Increment the number of zeroes in t
            num_zeroes += 1
        # If the current character of s is 1
        if s[i] == "1":
            # Set the current character of t to be 1
            t = "1"
            # Loop through the previous characters of s and t
            for j in range(i):
                # If the current character of s is 0 and the current character of t is 1
                if s[j] == "0" and t[j] == "1":
                    # Set the current character of t to be 0
                    t = "0"
                    # Break out of the loop
                    break
            # Add the current character of t to the end of the string t
            t += s[i]
        # Set the longest non-decreasing subsequence of t to be the maximum of the longest non-decreasing subsequence of t and the length of the current subsequence of t
        longest_subsequence_t[i] = max(longest_subsequence_t[i-1], num_zeroes)
        # Set the longest non-decreasing subsequence of s to be the maximum of the longest non-decreasing subsequence of s and the length of the current subsequence of s
        longest_subsequence_s[i] = max(longest_subsequence_s[i-1], longest_subsequence_s[i-1] + (1 if s[i] == "1" else 0))
    # Return the string t
    return t

