
def solve(s):
    # Initialize the output string
    output = ""
    
    # Iterate through the input string
    for c in s:
        # If the current character is a letter or a digit, add it to the output
        if c.isalpha() or c.isdigit():
            output += c
        # If the current character is a space, add a space to the output
        elif c == " ":
            output += " "
        # If the current character is a '<', do nothing
        elif c == "<":
            pass
        # If the current character is a '[', move the cursor to the start of the line
        elif c == "[":
            output = ""
        # If the current character is a ']', move the cursor to the end of the line
        elif c == "]":
            output += " "
    
    # Return the final output string
    return output.strip()

