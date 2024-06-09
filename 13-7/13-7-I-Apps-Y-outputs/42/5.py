
def solve(s, t):
    # Initialize variables
    max_len = 0
    curr_len = 0
    i = 0
    j = 0

    # Loop through the characters of s
    while i < len(s):
        # If the current character of s is in t, increment the current length
        if s[i] in t:
            curr_len += 1
            # If the current length is greater than the maximum length, update the maximum length
            if curr_len > max_len:
                max_len = curr_len
            # If the current character of s is not in t, reset the current length
        else:
            curr_len = 0
        i += 1

    return max_len

