
def solve(s):
    n = len(s)
    # Initialize the maximum length of the longest non-decreasing subsequence as 1
    max_len = 1
    # Initialize the number of zeroes in the string as 0
    num_zeroes = 0
    # Initialize the substring as an empty string
    substring = ""
    # Iterate over the characters of the string
    for i in range(n):
        # If the current character is a zero, increment the number of zeroes
        if s[i] == "0":
            num_zeroes += 1
        # If the current character is a one, check if the maximum length of the longest non-decreasing subsequence is greater than the current length
        elif s[i] == "1" and max_len > len(substring):
            # If the maximum length is greater than the current length, update the substring with the current character
            substring += s[i]
        # If the current character is a one and the maximum length is equal to the current length, check if the current character is greater than the last character in the substring
        elif s[i] == "1" and max_len == len(substring):
            # If the current character is greater than the last character in the substring, update the substring with the current character
            if s[i] > substring[-1]:
                substring += s[i]
    # Return the substring
    return substring

