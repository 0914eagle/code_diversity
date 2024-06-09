
def get_alternate_bracket_notation(s):
    # Initialize variables
    start, end = 0, 0
    notation = ""

    # Iterate through the string
    for i, char in enumerate(s):
        # If the character is an opening bracket, set the start index
        if char == "(":
            start = i
        # If the character is a closing bracket, set the end index
        elif char == ")":
            end = i
            # If the start and end indices are not the same, add the header to the notation
            if start != end:
                notation += f"{start},{end}:{end},{end}:"
            # If the start and end indices are the same, add the header to the notation
            else:
                notation += f"{start},{end}:{end},{end}:"

    # Return the notation
    return notation

