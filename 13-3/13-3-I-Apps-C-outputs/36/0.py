
def longest_sequence(s, i, j):
    # Initialize the longest sequence length to 0
    longest_seq_len = 0
    
    # Loop through the string from i to j
    for k in range(i, j):
        # Check if the current character is the same as the previous character
        if s[k] == s[k-1]:
            # If it is, increment the longest sequence length
            longest_seq_len += 1
        # If it is not, reset the longest sequence length to 0
        else:
            longest_seq_len = 0
    
    # Return the longest sequence length
    return longest_seq_len

