
def f1(s):
    # Initialize the output string
    output = ""
    
    # Iterate through the input string
    for char in s:
        # If the character is a letter or a digit, add it to the output
        if char.isalpha() or char.isdigit():
            output += char
        # If the character is a space, add a space to the output
        elif char == " ":
            output += " "
        # If the character is a '<', do nothing
        elif char == "<":
            pass
        # If the character is a '[', move the cursor to the beginning of the line
        elif char == "[":
            output = ""
        # If the character is a ']', move the cursor to the end of the line
        elif char == "]":
            output += " "
    
    # Return the final output string
    return output

def f2(s):
    # Initialize the output string
    output = ""
    
    # Iterate through the input string
    for char in s:
        # If the character is a letter or a digit, add it to the output
        if char.isalpha() or char.isdigit():
            output += char
        # If the character is a space, add a space to the output
        elif char == " ":
            output += " "
        # If the character is a '<', do nothing
        elif char == "<":
            pass
        # If the character is a '[', move the cursor to the beginning of the line
        elif char == "[":
            output = ""
        # If the character is a ']', move the cursor to the end of the line
        elif char == "]":
            output += " "
    
    # Return the final output string
    return output

if __name__ == '__main__':
    # Read the input string
    s = input()
    
    # Call the appropriate function based on the length of the input string
    if len(s) <= 1000:
        print(f1(s))
    else:
        print(f2(s))

