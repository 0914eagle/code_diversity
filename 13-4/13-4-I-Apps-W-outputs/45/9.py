
def solve(string):
    # Initialize the output string
    output = ""
    
    # Iterate through the input string
    for char in string:
        # If the current character is a letter or digit, add it to the output
        if char.isalpha() or char.isdigit():
            output += char
        # If the current character is a space, add a space to the output
        elif char == " ":
            output += " "
        # If the current character is a '<', do nothing
        elif char == "<":
            pass
        # If the current character is '[', move the cursor to the start of the line
        elif char == "[":
            output = ""
        # If the current character is ']', move the cursor to the end of the line
        elif char == "]":
            output += " "
    
    # Return the final output string
    return output.strip()

if __name__ == '__main__':
    # Read the input string
    string = input()
    
    # Call the solve function and print the result
    result = solve(string)
    print(result)

