
def is_nested(string: str) -> bool:
    
    # Initialize a stack to keep track of the brackets
    stack = []
    # Iterate through the string
    for char in string:
        # If the character is an opening bracket, push it to the stack
        if char == "[":
            stack.append(char)
        # If the character is a closing bracket, pop the top element from the stack
        elif char == "]":
            if len(stack) == 0:
                return False
            stack.pop()
    # If the stack is not empty, it means that there are unmatched brackets
    if len(stack) != 0:
        return False
    # If the stack is empty, it means that all the brackets are matched
    return True

