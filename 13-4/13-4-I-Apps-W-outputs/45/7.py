
def solve(string):
    # Initialize the output string
    output = ""
    
    # Iterate through the input string
    for char in string:
        # If the current character is a letter, number, or space, add it to the output
        if char.isalnum() or char == " ":
            output += char
        # If the current character is a '<', do nothing
        elif char == "<":
            pass
        # If the current character is '[', move the cursor to the beginning of the line
        elif char == "[":
            output = ""
        # If the current character is ']', move the cursor to the end of the line
        elif char == "]":
            output += " "
    
    # Return the final output string
    return output.strip()

if __name__ == '__main__':
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        string = input()
        print(solve(string))

