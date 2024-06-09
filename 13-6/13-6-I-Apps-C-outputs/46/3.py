
def get_color_code(n, p, s):
    # Check if the palette is valid
    if len(set(s)) != p:
        return "impossible"
    
    # Initialize the color code with the first string
    code = ["0" * n]
    
    # Iterate through the remaining strings
    for i in range(1, 2**n):
        # Find the previous string
        prev_str = code[i-1]
        
        # Find the next string by changing exactly one bit
        next_str = ""
        for j in range(n):
            if prev_str[j] == "0":
                next_str += "1"
            else:
                next_str += "0"
        
        # Check if the next string is in the palette
        if int(next_str, 2) in s:
            code.append(next_str)
        else:
            return "impossible"
    
    return "\n".join(code)

