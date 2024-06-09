
def solve(s):
    n = len(s)
    # Initialize the maximum length of the longest non-decreasing subsequence as 0
    max_len = 0
    # Initialize the index of the first element of the longest non-decreasing subsequence as -1
    first_index = -1
    # Initialize the number of zeroes in the string as 0
    num_zeroes = 0
    # Iterate over the characters of the string
    for i in range(n):
        # If the current character is a zero
        if s[i] == "0":
            # Increment the number of zeroes in the string
            num_zeroes += 1
        # If the current character is a one
        if s[i] == "1":
            # If the maximum length of the longest non-decreasing subsequence is 0
            if max_len == 0:
                # Set the maximum length of the longest non-decreasing subsequence to 1
                max_len = 1
                # Set the index of the first element of the longest non-decreasing subsequence to the current index
                first_index = i
            # If the maximum length of the longest non-decreasing subsequence is not 0
            else:
                # If the current index is less than the index of the first element of the longest non-decreasing subsequence
                if i < first_index:
                    # Set the maximum length of the longest non-decreasing subsequence to the current index minus the index of the first element of the longest non-decreasing subsequence
                    max_len = i - first_index
                    # Set the index of the first element of the longest non-decreasing subsequence to the current index
                    first_index = i
                # If the current index is greater than the index of the first element of the longest non-decreasing subsequence
                else:
                    # Set the maximum length of the longest non-decreasing subsequence to the current index minus the index of the first element of the longest non-decreasing subsequence
                    max_len = i - first_index + 1
    # Initialize a new string with the same length as the input string
    t = ["0"] * n
    # Iterate over the characters of the input string
    for i in range(n):
        # If the current character is a zero
        if s[i] == "0":
            # Set the current character of the output string to a zero
            t[i] = "0"
        # If the current character is a one
        if s[i] == "1":
            # Set the current character of the output string to a zero
            t[i] = "0"
            # If the current index is not the index of the first element of the longest non-decreasing subsequence
            if i != first_index:
                # Set the character at the index before the current index to a one
                t[i-1] = "1"
    # Return the output string
    return "".join(t)

