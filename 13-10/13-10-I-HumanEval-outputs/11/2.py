
def correct_bracketing(brackets: str) -> bool:
    
    # initialize a stack to keep track of opening brackets
    stack = []

    # loop through each character in the string
    for char in brackets:
        # if the character is an opening bracket, add it to the stack
        if char == "(":
            stack.append(char)
        # if the character is a closing bracket, remove the top opening bracket from the stack
        elif char == ")":
            if len(stack) == 0:
                return False
            stack.pop()

    # if the stack is empty, then every opening bracket has a corresponding closing bracket
    return len(stack) == 0

