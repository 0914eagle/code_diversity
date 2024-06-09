
def construct_color_code(n, p, palette):
    # Check if the palette is valid
    if len(set(palette)) != p:
        return "impossible"
    
    # Initialize the code with the first string
    code = ["0" * n]
    
    # Iterate through the remaining strings
    for i in range(1, 2**n):
        # Find the previous string in the code
        prev_string = code[i-1]
        
        # Find the next string in the code
        next_string = ""
        for j in range(n):
            # If the j-th bit of the previous string is 0, set the j-th bit of the next string to 1
            if prev_string[j] == "0":
                next_string += "1"
            # If the j-th bit of the previous string is 1, set the j-th bit of the next string to 0
            else:
                next_string += "0"
        
        # Check if the next string is in the palette
        if next_string not in palette:
            return "impossible"
        
        # Add the next string to the code
        code.append(next_string)
    
    return "\n".join(code)

