
def solve(s, t):
    # Initialize variables
    max_length = 0
    current_length = 0
    s_index = 0
    t_index = 0

    # Loop through s and t simultaneously
    while s_index < len(s) and t_index < len(t):
        # If the current character in s is the same as the current character in t, increment the current length
        if s[s_index] == t[t_index]:
            current_length += 1
            t_index += 1
        # If the current character in s is not the same as the current character in t, reset the current length
        else:
            current_length = 0
        # Update the maximum length if the current length is greater than the maximum length
        if current_length > max_length:
            max_length = current_length
        s_index += 1

    # Return the maximum length
    return max_length

