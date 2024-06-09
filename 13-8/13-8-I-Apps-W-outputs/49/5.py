
def solve(s):
    # Initialize a dictionary to store the opening and closing brackets
    brackets = {
        "<": ">",
        "{": "}",
        "[": "]",
        "(": ")"
    }
    
    # Initialize a stack to keep track of the opening brackets
    stack = []
    
    # Iterate through the string
    for char in s:
        # If the character is an opening bracket, push it to the stack
        if char in brackets:
            stack.append(char)
        # If the character is a closing bracket, pop the top element from the stack and check if it matches the closing bracket
        else:
            if not stack or brackets[stack.pop()] != char:
                return "Impossible"
    
    # If the stack is not empty, it means that not all opening brackets have a matching closing bracket
    if stack:
        return "Impossible"
    
    # If the stack is empty, return the length of the string
    return len(s)

