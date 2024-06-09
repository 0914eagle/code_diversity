
def is_nested(string: str) -> bool:
    
    # Check if the input string contains only square brackets
    if not string.isalnum():
        # If the input string is empty, return False
        if not string:
            return False
        # Initialize a stack to keep track of the number of opening brackets
        stack = []
        # Iterate through the string
        for char in string:
            # If the current character is an opening bracket, push it to the stack
            if char == '[':
                stack.append(char)
            # If the current character is a closing bracket, pop an opening bracket from the stack
            elif char == ']':
                if not stack:
                    return False
                stack.pop()
        # If the stack is empty, return True
        if not stack:
            return True
        # If the stack is not empty, return False
        return False
    # If the input string contains any non-bracket characters, return False
    else:
        return False

