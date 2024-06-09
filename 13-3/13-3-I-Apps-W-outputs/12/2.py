
def solve(s):
    n = len(s)
    # Initialize the maximum length of the longest non-decreasing subsequence as 1
    max_len = 1
    # Initialize the length of the longest non-decreasing subsequence as 1
    length = 1
    # Initialize the previous element as -1
    prev = -1
    # Initialize the count of zeroes as 0
    count = 0
    # Initialize the result string as an empty string
    result = ""
    # Iterate over the characters of the input string
    for i in range(n):
        # If the current character is 0
        if s[i] == "0":
            # Increment the count of zeroes
            count += 1
            # If the current character is not equal to the previous character
            if s[i] != prev:
                # Update the length of the longest non-decreasing subsequence
                length = max(length, count)
                # Update the maximum length of the longest non-decreasing subsequence
                max_len = max(max_len, length)
                # Reset the count of zeroes
                count = 0
            # Update the previous element
            prev = s[i]
        # If the current character is 1
        else:
            # Update the count of zeroes
            count += 1
            # If the current character is not equal to the previous character
            if s[i] != prev:
                # Update the length of the longest non-decreasing subsequence
                length = max(length, count)
                # Update the maximum length of the longest non-decreasing subsequence
                max_len = max(max_len, length)
                # Reset the count of zeroes
                count = 0
            # Update the previous element
            prev = s[i]
    
    # If the last character is 0
    if s[n-1] == "0":
        # Increment the count of zeroes
        count += 1
        # Update the length of the longest non-decreasing subsequence
        length = max(length, count)
        # Update the maximum length of the longest non-decreasing subsequence
        max_len = max(max_len, length)
    
    # Iterate over the characters of the input string
    for i in range(n):
        # If the current character is 0
        if s[i] == "0":
            # Add the current character to the result string
            result += "0"
        # If the current character is 1
        else:
            # Add the current character to the result string
            result += "1"
    
    # Return the result string
    return result

