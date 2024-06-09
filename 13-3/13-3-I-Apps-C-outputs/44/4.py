
def convert_brackets(s):
    # Initialize variables
    new_string = ""
    start_index = 0
    end_index = 0

    # Iterate through the string
    for i, char in enumerate(s):
        # If the character is an opening bracket, set the start index
        if char == "(":
            start_index = i
        # If the character is a closing bracket, set the end index
        elif char == ")":
            end_index = i
            # Add the header to the new string
            new_string += f"{start_index},{end_index}:{start_index},{end_index}:"
            # Reset the start and end indices
            start_index = 0
            end_index = 0

    # Return the new string
    return new_string

