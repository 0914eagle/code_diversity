
def correct_bracketing(brackets: str) -> bool:
    
    # Initialize a stack to keep track of opening brackets
    stack = []

    # Loop through each character in the string
    for char in brackets:
        # If the character is an opening bracket, push it onto the stack
        if char == "<":
            stack.append(char)
        # If the character is a closing bracket, try to pop an opening bracket from the stack
        elif char == ">":
            try:
                stack.pop()
            # If the stack is empty or there is no matching opening bracket, return False
            except IndexError:
                return False

    # If the stack is empty, return True, otherwise return False
    return not stack

