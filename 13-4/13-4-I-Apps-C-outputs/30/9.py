
def solve(n, s):
    # Initialize the result variable
    result = 0

    # Initialize a stack to keep track of the opening and closing brackets
    stack = []

    # Iterate through the string
    for i in range(n):
        # If the current character is an opening bracket, push it to the stack
        if s[i] == "(":
            stack.append(s[i])
        # If the current character is a closing bracket, pop the top element from the stack
        # and check if it is an opening bracket
        elif s[i] == ")":
            if not stack or stack[-1] != "(":
                return -1
            stack.pop()

    # If the stack is not empty, it means that there are unmatched brackets
    if stack:
        return -1

    # Return the result
    return result

