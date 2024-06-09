
def solve(s):
    # Initialize the maximum length of the substring as 0
    max_len = 0
    
    # Loop through each substring of the input string
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Check if the substring starts with 'A' and ends with 'Z'
            if s[i] == 'A' and s[j] == 'Z':
                # If the substring is longer than the current maximum, update the maximum
                if j - i + 1 > max_len:
                    max_len = j - i + 1
    
    # Return the maximum length
    return max_len

