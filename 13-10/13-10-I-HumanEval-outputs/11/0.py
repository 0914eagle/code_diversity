
def correct_bracketing(brackets: str) -> bool:
    
    # Initialize a stack to keep track of the opening brackets
    stack = []

    # Loop through each character in the string
    for char in brackets:
        # If the character is an opening bracket, push it to the stack
        if char == "(":
            stack.append(char)
        # If the character is a closing bracket, pop an opening bracket from the stack
        elif char == ")":
            if len(stack) == 0:
                return False
            stack.pop()

    # If the stack is empty, then every opening bracket has a corresponding closing bracket
    return len(stack) == 0

