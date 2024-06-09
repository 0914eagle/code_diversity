
def get_color_code(n, p, s):
    # Initialize an empty list to store the color code
    code = []
    
    # Check if the palette is valid
    if len(set(s)) != p:
        return "impossible"
    
    # Check if the palette is a subset of {1, 2, ..., n}
    if not set(s).issubset({i for i in range(1, n+1)}):
        return "impossible"
    
    # Initialize the first string with all 0s
    current_string = "0" * n
    code.append(current_string)
    
    # Iterate through the palette
    for i in range(p):
        # Get the current string and its binary negation
        current_string = code[-1]
        negated_string = current_string[:]
        for j in range(n):
            if negated_string[j] == "0":
                negated_string[j] = "1"
            else:
                negated_string[j] = "0"
        
        # Check if the negated string is already in the code
        if negated_string in code:
            return "impossible"
        
        # Add the negated string to the code
        code.append(negated_string)
    
    # Return the code
    return "\n".join(code)

