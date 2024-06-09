
def solve(s, k):
    n = len(s)
    if k > n:
        return ""
    
    # Initialize the result with the first k characters of s
    result = s[:k]
    
    # Iterate through the remaining characters of s
    for i in range(k, n):
        # If the current character is lexicographically smaller than the last character of the result
        if s[i] < result[-1]:
            # Add the current character to the result
            result += s[i]
    
    return result

