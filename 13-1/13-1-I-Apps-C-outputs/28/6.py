
def f1(s):
    # Initialize variables
    stack = []
    notation = ""
    
    # Iterate through the string
    for i, char in enumerate(s):
        if char == "(":
            # If we encounter an open bracket, push the index to the stack
            stack.append(i)
        elif char == ")":
            # If we encounter a closed bracket, pop the top index from the stack
            start = stack.pop()
            # Append the header to the notation string
            notation += str(start) + "," + str(i) + ":"
    
    # Return the notation string
    return notation

