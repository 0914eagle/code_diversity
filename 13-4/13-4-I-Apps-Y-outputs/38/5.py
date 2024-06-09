
def solve(s):
    # Initialize the maximum length of the substring as 0
    max_len = 0
    
    # Loop through each substring of the input string
    for i in range(len(s)):
        for j in range(i, len(s)):
            # If the substring starts with 'A' and ends with 'Z', check if its length is greater than the current maximum length
            if s[i] == 'A' and s[j] == 'Z':
                curr_len = j - i + 1
                if curr_len > max_len:
                    max_len = curr_len
    
    # Return the maximum length
    return max_len

