
def correct_bracketing(brackets: str) -> bool:
    
    # Initialize a stack to keep track of the opening brackets
    stack = []

    # Iterate through the string
    for char in brackets:
        # If the current character is an opening bracket, push it onto the stack
        if char == "(":
            stack.append(char)
        # If the current character is a closing bracket, pop an opening bracket from the stack
        elif char == ")":
            if not stack:
                return False
            stack.pop()

    # If the stack is empty, then every opening bracket has a corresponding closing bracket
    return not stack

