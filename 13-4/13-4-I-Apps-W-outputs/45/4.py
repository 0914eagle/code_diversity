
def f1(s):
    # Initialize the output string
    output = ""
    
    # Iterate through the input string
    for i in range(len(s)):
        # If the current character is a letter, number, or space, add it to the output
        if s[i].isalnum() or s[i] == " ":
            output += s[i]
        # If the current character is '<', move the cursor back one position
        elif s[i] == "<":
            if len(output) > 0:
                output = output[:-1]
        # If the current character is '[', move the cursor to the beginning of the line
        elif s[i] == "[":
            output = ""
        # If the current character is ']', move the cursor to the end of the line
        elif s[i] == "]":
            output += " "
    
    # Return the final output string
    return output

def f2(s):
    # Initialize the output string
    output = ""
    
    # Iterate through the input string
    for i in range(len(s)):
        # If the current character is a letter, number, or space, add it to the output
        if s[i].isalnum() or s[i] == " ":
            output += s[i]
        # If the current character is '<', move the cursor back one position
        elif s[i] == "<":
            if len(output) > 0:
                output = output[:-1]
        # If the current character is '[', move the cursor to the beginning of the line
        elif s[i] == "[":
            output = ""
        # If the current character is ']', move the cursor to the end of the line
        elif s[i] == "]":
            output += " "
    
    # Return the final output string
    return output

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(f1(s))
        print(f2(s))

