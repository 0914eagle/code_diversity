
def solve(s):
    n = len(s)
    # Initialize the longest non-decreasing subsequence of s and t
    longest_non_decreasing_subsequence_s = [1] * n
    longest_non_decreasing_subsequence_t = [1] * n
    
    # Loop through the string and calculate the longest non-decreasing subsequence
    for i in range(1, n):
        for j in range(i):
            if s[i] >= s[j] and longest_non_decreasing_subsequence_s[i] < longest_non_decreasing_subsequence_s[j] + 1:
                longest_non_decreasing_subsequence_s[i] = longest_non_decreasing_subsequence_s[j] + 1
    
    # Loop through the string and calculate the longest non-decreasing subsequence
    for i in range(1, n):
        for j in range(i):
            if s[i] >= s[j] and longest_non_decreasing_subsequence_t[i] < longest_non_decreasing_subsequence_t[j] + 1:
                longest_non_decreasing_subsequence_t[i] = longest_non_decreasing_subsequence_t[j] + 1
    
    # Find the maximum length of the longest non-decreasing subsequence
    max_length = max(longest_non_decreasing_subsequence_s)
    
    # Initialize the result string
    result = ""
    
    # Loop through the string and find the indices with the maximum length of the longest non-decreasing subsequence
    for i in range(n):
        if longest_non_decreasing_subsequence_s[i] == max_length:
            result += "1"
        else:
            result += "0"
    
    return result

