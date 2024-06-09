
def get_rbs(s):
    # Initialize a stack to keep track of opening brackets
    stack = []
    # Initialize a counter for the number of replacements
    count = 0
    # Iterate through the string
    for char in s:
        # If the character is an opening bracket, push it to the stack
        if char in ["<", "{", "(", "["]:
            stack.append(char)
        # If the character is a closing bracket, pop the top element from the stack
        # and check if it is the matching opening bracket
        elif char in [">", "}", ")", "]"]:
            if not stack or stack[-1] != match(char):
                # If the top element is not the matching opening bracket, increase the counter and push the character to the stack
                count += 1
                stack.append(char)
            else:
                # If the top element is the matching opening bracket, pop it from the stack
                stack.pop()
    # If the stack is not empty, it means that not all opening brackets have a matching closing bracket, so return -1
    if stack:
        return -1
    # Return the counter
    return count

# Define a dictionary to map each closing bracket to its matching opening bracket
match = {"<": ">", "{": "}", "(": ")", "]": "["}

s = input()
result = get_rbs(s)
if result == -1:
    print("Impossible")
else:
    print(result)

