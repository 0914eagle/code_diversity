
def f1(s):
    # Initialize the output string
    output = ""
    
    # Iterate through the input string
    for c in s:
        # If the current character is a letter or a digit, add it to the output
        if c.isalpha() or c.isdigit():
            output += c
        # If the current character is a '<', do nothing
        elif c == "<":
            pass
        # If the current character is a '[', move the cursor to the beginning of the line
        elif c == "[":
            output = ""
        # If the current character is a ']', move the cursor to the end of the line
        elif c == "]":
            output += " "
    
    # Return the final output string
    return output

def f2(s):
    # Initialize the output string
    output = ""
    
    # Iterate through the input string
    for c in s:
        # If the current character is a letter or a digit, add it to the output
        if c.isalpha() or c.isdigit():
            output += c
        # If the current character is a '<', do nothing
        elif c == "<":
            pass
        # If the current character is a '[', move the cursor to the beginning of the line
        elif c == "[":
            output = ""
        # If the current character is a ']', move the cursor to the end of the line
        elif c == "]":
            output += " "
    
    # Return the final output string
    return output

if __name__ == '__main__':
    # Read the input string
    s = input()
    
    # Call the appropriate function based on the input string length
    if len(s) <= 1000:
        print(f1(s))
    else:
        print(f2(s))

