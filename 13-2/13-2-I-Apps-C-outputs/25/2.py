
def longest_sequence(s, i, j):
    # Initialize the longest sequence length to 0
    longest = 0

    # Loop through the string from i to j
    for k in range(i, j):
        # If the current character is the same as the previous character
        if s[k] == s[k-1]:
            # Increment the longest sequence length
            longest += 1
        # If the current character is not the same as the previous character
        else:
            # Break out of the loop
            break

    # Return the longest sequence length
    return longest

