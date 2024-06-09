
def f1(string):
    # Initialize the output string
    output = ""
    
    # Iterate through the input string
    for char in string:
        # If the current character is a letter or a digit, add it to the output
        if char.isalpha() or char.isdigit():
            output += char
        # If the current character is a space, add a space to the output
        elif char == " ":
            output += " "
        # If the current character is a '<', do nothing
        elif char == "<":
            pass
        # If the current character is a '[', move the cursor to the start of the line
        elif char == "[":
            output = ""
        # If the current character is a ']', move the cursor to the end of the line
        elif char == "]":
            output += " "
    
    # Return the final output string
    return output

def f2(string):
    # Initialize the output string
    output = ""
    
    # Iterate through the input string
    for char in string:
        # If the current character is a letter or a digit, add it to the output
        if char.isalpha() or char.isdigit():
            output += char
        # If the current character is a space, add a space to the output
        elif char == " ":
            output += " "
        # If the current character is a '<', do nothing
        elif char == "<":
            pass
        # If the current character is a '[', move the cursor to the start of the line
        elif char == "[":
            output = ""
        # If the current character is a ']', move the cursor to the end of the line
        elif char == "]":
            output += " "
    
    # Return the final output string
    return output

if __name__ == '__main__':
    # Read the input string
    string = input()
    
    # Call the appropriate function based on the length of the input string
    if len(string) <= 1000:
        output = f1(string)
    else:
        output = f2(string)
    
    # Print the final output string
    print(output)

