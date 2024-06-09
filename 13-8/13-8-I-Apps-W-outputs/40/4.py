
def solve(s, t):
    # Initialize a counter for the maximum number of occurrences
    max_occurrences = 0
    # Initialize a variable to store the result string
    result = ""

    # Loop through each character in the input string
    for i in range(len(s)):
        # If the current character is a question mark, replace it with each character in the target string
        if s[i] == "?":
            for j in range(len(t)):
                # Create a new string by replacing the current question mark with the jth character of the target string
                new_string = s[:i] + t[j] + s[i+1:]
                # Check if the new string has the maximum number of occurrences of the target string
                occurrences = new_string.count(t)
                if occurrences > max_occurrences:
                    # If so, update the maximum number of occurrences and the result string
                    max_occurrences = occurrences
                    result = new_string
        # If the current character is not a question mark, add it to the result string
        else:
            result += s[i]

    # Return the result string
    return result

