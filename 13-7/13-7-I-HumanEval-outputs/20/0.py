
def is_nested(string: str) -> bool:
    
    # Initialize a stack to keep track of the open brackets
    stack = []

    # Iterate through the string
    for char in string:
        # If the current character is an opening bracket, push it to the stack
        if char == "[":
            stack.append(char)
        # If the current character is a closing bracket, pop an opening bracket from the stack
        elif char == "]":
            if len(stack) == 0:
                return False
            stack.pop()

    # If the stack is empty, all brackets are nested correctly
    return len(stack) == 0

