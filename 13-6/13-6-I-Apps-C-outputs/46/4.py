
def get_color_code(n, p, palette):
    # Check if the palette is valid
    if len(set(palette)) != len(palette):
        return "impossible"
    
    # Initialize the color code with the first string
    code = ["0" * n]
    
    # Iterate through the remaining strings
    for i in range(1, 2**n):
        # Find the previous string in the code
        prev_string = code[i-1]
        
        # Find the number of bits that differ between the previous string and the current string
        diff = 0
        for j in range(n):
            if prev_string[j] != code[i][j]:
                diff += 1
        
        # Check if the difference is in the palette
        if diff not in palette:
            return "impossible"
        
        # Add the current string to the code
        code.append(code[i-1][:diff] + "1" + code[i-1][diff+1:])
    
    return "\n".join(code)

