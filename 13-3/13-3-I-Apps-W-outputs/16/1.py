
def solve(s, k):
    n = len(s)
    if k > n:
        return ""
    
    # Initialize the result with the first k characters of s
    result = s[:k]
    
    # Iterate over the remaining characters of s
    for i in range(k, n):
        # If the current character is lexicographically smaller than the last character of the result, replace the last character of the result with the current character
        if s[i] < result[-1]:
            result = result[:-1] + s[i]
    
    return result

