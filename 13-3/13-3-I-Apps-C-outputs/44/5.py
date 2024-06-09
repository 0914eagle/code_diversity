
def convert_brackets(s):
    # Initialize variables
    start = 0
    end = 0
    new_string = ""

    # Iterate through the input string
    for i, char in enumerate(s):
        # If the character is an opening bracket, set the start index
        if char == "(":
            start = i
        # If the character is a closing bracket, set the end index
        elif char == ")":
            end = i
            # Check if the start and end indices are not the same
            if start != end:
                # Add the header to the new string
                new_string += str(start) + "," + str(end) + ":"
                # Set the start index to the end index
                start = end

    # Return the new string
    return new_string

