
def construct_color_code(n, p, palettes):
    # Check if the palette is valid
    if len(set(palettes)) != len(palettes):
        return "impossible"
    
    # Initialize the color code with the first element
    color_code = [0] * 2**n
    color_code[0] = palettes[0]
    
    # Fill in the remaining elements
    for i in range(1, 2**n):
        # Find the next element in the color code
        next_element = (color_code[i-1] + 1) % len(palettes)
        
        # Check if the next element is in the palette
        if next_element not in palettes:
            return "impossible"
        
        # Add the next element to the color code
        color_code[i] = next_element
    
    return color_code

