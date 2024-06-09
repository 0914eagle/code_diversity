
def f1(s):
    # Initialize the output string
    output = ""
    
    # Iterate through the input string
    for c in s:
        # If the current character is a letter, number, or space, append it to the output
        if c.isalnum() or c.isspace():
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
        # If the current character is a letter, number, or space, append it to the output
        if c.isalnum() or c.isspace():
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
    t = int(input())
    for _ in range(t):
        s = input()
        print(f1(s))
        print(f2(s))

