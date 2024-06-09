
def get_alternative_bracket_notation(s):
    # Initialize variables
    notation = ""
    start = 0
    end = 0

    # Iterate through the string
    for i, char in enumerate(s):
        # If the character is an open parenthesis, set the start index
        if char == "(":
            start = i
        # If the character is a closed parenthesis, set the end index
        elif char == ")":
            end = i
            # If the start and end indices are not the same, add the header to the notation
            if start != end:
                notation += str(start) + "," + str(end) + ":"
            # Reset the start and end indices
            start = 0
            end = 0

    # Return the notation
    return notation

