
def is_nested(string: str) -> bool:
    
    # Initialize a stack to keep track of the brackets
    stack = []

    # Iterate through the string
    for char in string:
        # If the current character is a closing bracket, check if it is balanced
        if char == "]":
            # If the stack is empty or the top of the stack is not a opening bracket, return False
            if not stack or stack[-1] != "[":
                return False
            # Otherwise, pop the top of the stack
            stack.pop()
        # If the current character is an opening bracket, push it onto the stack
        else:
            stack.append(char)

    # If the stack is not empty, return False
    if stack:
        return False

    # If the stack is empty, return True
    return True

