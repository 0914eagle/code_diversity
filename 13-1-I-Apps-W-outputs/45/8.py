
def solve(n, c):
    # Initialize the string with the first character
    string = ["a"]

    # Iterate over the remaining characters
    for i in range(1, n):
        # Check if the current character is already present in the string
        if string[i-1] in string:
            # If it is, append the next character to the string
            string.append(chr(ord(string[i-1]) + 1))
        else:
            # If it's not, append the current character to the string
            string.append(string[i-1])

    # Return the repaired string
    return "".join(string)

