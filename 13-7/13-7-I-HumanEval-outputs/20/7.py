
def is_nested(string: str) -> bool:
    
    # Initialize a stack to keep track of the brackets
    stack = []

    # Iterate through the string
    for char in string:
        # If the current character is an opening bracket, push it to the stack
        if char == "[":
            stack.append(char)
        # If the current character is a closing bracket, check if it is balanced
        elif char == "]":
            # If the stack is empty, the brackets are not balanced
            if len(stack) == 0:
                return False
            # If the top of the stack is an opening bracket, pop it and continue
            if stack[-1] == "[":
                stack.pop()
            # If the top of the stack is a closing bracket, the brackets are not balanced
            else:
                return False

    # If the stack is not empty, the brackets are not balanced
    if len(stack) != 0:
        return False

    # If the string is empty, the brackets are not nested
    if len(string) == 0:
        return False

    # Check if there is a valid subsequence of brackets where at least one bracket in the subsequence is nested
    for i in range(len(string) - 1):
        # If the current character is an opening bracket, check if it is nested
        if string[i] == "[":
            # If the next character is also an opening bracket, the brackets are nested
            if string[i + 1] == "[":
                return True

    # If no nested brackets are found, return False
    return False

