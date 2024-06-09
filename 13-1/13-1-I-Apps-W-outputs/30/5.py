
def solve(s):
    # Initialize variables
    min_length = len(s)
    compressed_version = ""

    # Iterate through the string
    for i in range(len(s)):
        # Check if the current character is the same as the previous character
        if i > 0 and s[i] == s[i-1]:
            # If it is, continue the current compressed version
            continue
        else:
            # If it's not, start a new compressed version
            compressed_version += str(i+1) + s[i]

    # Return the minimum length
    return len(compressed_version)

