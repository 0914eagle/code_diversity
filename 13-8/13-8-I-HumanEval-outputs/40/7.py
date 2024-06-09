
def is_nested(string: str) -> bool:
    
    # Initialize a stack to keep track of the brackets
    stack = []

    # Iterate through the string
    for char in string:
        # If the current character is an opening bracket, push it to the stack
        if char == "[":
            stack.append(char)
        # If the current character is a closing bracket, pop the top element from the stack
        elif char == "]":
            if len(stack) == 0:
                return False
            stack.pop()

    # If the stack is not empty, it means that there is an unmatched opening bracket
    if len(stack) != 0:
        return False

    # If the string is empty, it means that there are no valid substrings
    if len(string) == 0:
        return False

    # If the string has only one character, it means that there is no nesting
    if len(string) == 1:
        return False

    # Check if there is a valid substring of brackets
    for i in range(len(string) - 1):
        if string[i] == "[" and string[i + 1] == "[":
            return True

    return False

