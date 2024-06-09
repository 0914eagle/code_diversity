
def convert_brackets(s):
    # Initialize variables
    alt_notation = ""
    stack = []
    
    # Iterate through the string
    for i, char in enumerate(s):
        # If the character is an opening bracket, push the index to the stack
        if char == "(":
            stack.append(i)
        # If the character is a closing bracket, pop the top index from the stack
        # and use it to create a header in the alternative notation
        elif char == ")":
            start = stack.pop()
            end = i
            header = f"{start},{end}:{start},{end}:"
            alt_notation += header
    
    # Return the alternative notation
    return alt_notation

