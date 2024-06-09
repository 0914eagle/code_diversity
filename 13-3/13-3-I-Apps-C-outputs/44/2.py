
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
            # Append the header to the new string
            new_string += str(start_index) + "," + str(end_index) + ":"
            # Set the start index to the end index + 1
            start_index = end_index + 1

    # Return the new string
    return new_string

