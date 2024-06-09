
def solve(s):
    # Initialize variables
    min_length = len(s)
    compressed_version = ""

    # Iterate through the string
    for i in range(len(s)):
        # Check if the current character is the same as the previous character
        if i > 0 and s[i] == s[i-1]:
            # If it is, increment the count
            count += 1
        else:
            # If it's not, add the count and the character to the compressed version
            if count > 0:
                compressed_version += str(count) + s[i-1]
            count = 1

    # Add the final count and character
    if count > 0:
        compressed_version += str(count) + s[len(s)-1]

    # Return the length of the compressed version
    return len(compressed_version)

