
def get_color_code(n, p, palettes):
    # Check if the palette is valid
    if len(set(palettes)) != len(palettes):
        return "impossible"
    
    # Initialize the color code with the first string
    color_code = ["0" * n]
    
    # Iterate through the remaining strings
    for i in range(1, 2**n):
        # Find the previous string
        prev_string = color_code[i-1]
        
        # Find the next string by changing exactly one bit
        next_string = ""
        for j in range(n):
            if prev_string[j] == "0":
                next_string += "1"
            else:
                next_string += "0"
        
        # Check if the next string is valid
        if next_string in color_code:
            return "impossible"
        
        # Add the next string to the color code
        color_code.append(next_string)
    
    return "\n".join(color_code)

