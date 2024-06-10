
def correct_bracketing(brackets: str) -> bool:
    
    # Initialize a stack to keep track of opening brackets
    stack = []

    # Iterate through the string
    for char in brackets:
        # If the current character is an opening bracket, push it onto the stack
        if char == "(":
            stack.append(char)
        # If the current character is a closing bracket, check if it has a corresponding opening bracket
        elif char == ")":
            # If the stack is empty, there is no corresponding opening bracket, so return False
            if len(stack) == 0:
                return False
            # Pop the top character from the stack and check if it is an opening bracket
            top_char = stack.pop()
            if top_char != "(":
                return False

    # If we reach the end of the string and the stack is not empty, there is no corresponding closing bracket for the opening bracket, so return False
    if len(stack) > 0:
        return False

    # If we reach the end of the string and the stack is empty, all opening brackets have a corresponding closing bracket, so return True
    return True

