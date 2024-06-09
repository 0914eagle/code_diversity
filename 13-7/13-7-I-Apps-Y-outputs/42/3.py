
def solve(s, t):
    # Initialize variables
    max_length = 0
    s_len = len(s)
    t_len = len(t)

    # Iterate over the length of the substring
    for length in range(t_len, s_len + 1):
        # Initialize variables
        start = 0
        end = length - 1

        # Iterate over the starting index of the substring
        while start <= s_len - length:
            # Check if the substring is a subsequence of s
            if is_subsequence(s[start:end], t):
                # Update the maximum length if necessary
                max_length = max(max_length, length)

            # Increment the starting index
            start += 1

    # Return the maximum length
    return max_length

# Check if t is a subsequence of s
def is_subsequence(s, t):
    # Initialize variables
    s_index = 0
    t_index = 0

    # Iterate over the characters of s
    while s_index < len(s) and t_index < len(t):
        # Check if the characters match
        if s[s_index] == t[t_index]:
            # Increment the indices
            s_index += 1
            t_index += 1
        else:
            # Increment only the s_index
            s_index += 1

    # Check if all characters of t have been matched
    return t_index == len(t)

