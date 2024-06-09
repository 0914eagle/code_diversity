
def solve(s):
    n = len(s)
    # Initialize the maximum length of the longest non-decreasing subsequence as 1
    max_len = 1
    # Initialize the length of the longest non-decreasing subsequence of the current substring as 1
    curr_len = 1
    # Initialize the length of the longest non-decreasing subsequence of the previous substring as 1
    prev_len = 1
    # Initialize the number of zeroes in the current substring as 0
    num_zeroes = 0
    # Initialize the number of zeroes in the previous substring as 0
    prev_num_zeroes = 0
    # Initialize the substring as empty
    substring = ""
    # Initialize the previous substring as empty
    prev_substring = ""
    # Iterate over the characters of the input string
    for i in range(n):
        # If the current character is a zero
        if s[i] == "0":
            # Increment the number of zeroes in the current substring
            num_zeroes += 1
        # If the current character is a one
        else:
            # If the number of zeroes in the current substring is greater than the maximum length of the longest non-decreasing subsequence
            if num_zeroes > max_len:
                # Update the maximum length of the longest non-decreasing subsequence
                max_len = num_zeroes
            # If the number of zeroes in the current substring is equal to the maximum length of the longest non-decreasing subsequence
            if num_zeroes == max_len:
                # Update the substring
                substring = s[i-num_zeroes+1:i+1]
            # Reset the number of zeroes in the current substring
            num_zeroes = 0
        # If the current character is a zero
        if s[i] == "0":
            # If the number of zeroes in the previous substring is greater than the maximum length of the longest non-decreasing subsequence
            if prev_num_zeroes > max_len:
                # Update the maximum length of the longest non-decreasing subsequence
                max_len = prev_num_zeroes
            # If the number of zeroes in the previous substring is equal to the maximum length of the longest non-decreasing subsequence
            if prev_num_zeroes == max_len:
                # Update the substring
                prev_substring = s[i-prev_num_zeroes+1:i]
            # Reset the number of zeroes in the previous substring
            prev_num_zeroes = 0
        # If the current character is a one
        else:
            # Increment the number of zeroes in the previous substring
            prev_num_zeroes += 1
        # If the current character is the last character of the input string
        if i == n-1:
            # If the number of zeroes in the current substring is greater than the maximum length of the longest non-decreasing subsequence
            if num_zeroes > max_len:
                # Update the maximum length of the longest non-decreasing subsequence
                max_len = num_zeroes
            # If the number of zeroes in the current substring is equal to the maximum length of the longest non-decreasing subsequence
            if num_zeroes == max_len:
                # Update the substring
                substring = s[i-num_zeroes+1:i+1]
    # Return the substring
    return substring

