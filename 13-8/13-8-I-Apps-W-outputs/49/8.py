
def get_rbs(s):
    # Initialize a stack to keep track of the opening brackets
    stack = []
    # Initialize a count of the number of replacements needed
    replacements = 0

    for char in s:
        # If the character is an opening bracket, push it onto the stack
        if char in ["<", "{", "[", "("]:
            stack.append(char)
        # If the character is a closing bracket, pop the top element from the stack and check if it is the corresponding opening bracket
        elif char in [">", "}", "]", ")"]:
            # If the stack is empty, the string is not RBS and we return -1
            if not stack:
                return "Impossible"
            # If the top element of the stack is not the corresponding opening bracket, we need to replace it with the correct opening bracket and increment the number of replacements
            if stack[-1] != {"><": {"><", "}": "{", "]": "[", ")": "("}[char]:
                replacements += 1
                stack[-1] = {"><": {"><", "}": "{", "]": "[", ")": "("}[char]
        # If the character is not a bracket, return -1
        else:
            return "Impossible"

    # If the string is RBS and all the brackets are balanced, return the number of replacements needed
    if not stack and replacements % 2 == 0:
        return replacements // 2
    # If the string is not RBS or the number of replacements is odd, return -1
    else:
        return "Impossible"

