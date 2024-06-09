
def get_alternative_bracket_notation(s):
    # Initialize variables
    notation = ""
    stack = []
    
    # Iterate through the string
    for i, char in enumerate(s):
        # If the character is an opening bracket, push the index to the stack
        if char == "(":
            stack.append(i)
        # If the character is a closing bracket, pop the top index from the stack and form a header
        elif char == ")":
            start = stack.pop()
            end = i
            notation += f"{start},{end}:{s[start+1:end]},"
    
    # Return the notation string
    return notation[:-1]

