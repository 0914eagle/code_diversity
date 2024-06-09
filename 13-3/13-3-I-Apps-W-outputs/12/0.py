
def solve(s):
    n = len(s)
    # Initialize the maximum length of the longest non-decreasing subsequence as 0
    max_len = 0
    # Initialize the starting index of the longest non-decreasing subsequence as 0
    start_index = 0
    # Initialize the number of zeroes in the string as 0
    num_zeroes = 0
    # Iterate over the characters of the string
    for i in range(n):
        # If the current character is a zero, increment the number of zeroes
        if s[i] == "0":
            num_zeroes += 1
        # If the current character is a one, check if the length of the longest non-decreasing subsequence is greater than the current maximum length
        elif s[i] == "1":
            if max_len < i - start_index:
                # If the length of the longest non-decreasing subsequence is greater than the current maximum length, update the maximum length and the starting index of the longest non-decreasing subsequence
                max_len = i - start_index
                start_index = start_index
    # Return the string with the maximum number of zeroes and the length of the longest non-decreasing subsequence for each substring
    return "0" * num_zeroes + "1" * max_len

