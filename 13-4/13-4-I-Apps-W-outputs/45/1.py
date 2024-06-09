
def solve(string):
    # Initialize an empty string to store the final output
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
        # If the current character is a '[', move the cursor to the start of the line
        elif char == "[":
            output = ""
        # If the current character is a ']', move the cursor to the end of the line
        elif char == "]":
            output += " "
    
    # Return the final output
    return output

def main():
    # Read the input string
    string = input()
    
    # Solve the problem
    output = solve(string)
    
    # Print the output
    print(output)

if __name__ == '__main__':
    main()

