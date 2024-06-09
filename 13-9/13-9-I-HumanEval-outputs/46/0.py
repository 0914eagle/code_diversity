
def correct_bracketing(brackets: str) -> bool:
    
    # Initialize a stack to keep track of the opening brackets
    stack = []

    # Iterate through the string
    for char in brackets:
        # If we encounter an opening bracket, push it to the stack
        if char == "<":
            stack.append(char)
        # If we encounter a closing bracket, pop an opening bracket from the stack
        elif char == ">":
            if len(stack) == 0:
                return False
            stack.pop()

    # If the stack is empty, then we have a valid string
    return len(stack) == 0

