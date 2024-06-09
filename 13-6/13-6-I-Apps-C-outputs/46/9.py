
def get_color_code(n, p, palette):
    # Check if the palette is valid
    if len(set(palette)) != len(palette):
        return "impossible"
    
    # Initialize the color code with the first string
    code = ["0" * n]
    
    # Iterate through the remaining strings
    for i in range(1, 2**n):
        # Find the previous string
        prev_string = code[i-1]
        
        # Find the next string by changing the last bit
        next_string = prev_string[:-1] + str(int(prev_string[-1]) ^ 1)
        
        # Check if the next string is in the palette
        if next_string not in palette:
            return "impossible"
        
        # Add the next string to the code
        code.append(next_string)
    
    return "\n".join(code)

