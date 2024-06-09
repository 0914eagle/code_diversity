
def get_color_code(n, p, palettes):
    # Check if the input is valid
    if n < 1 or n > 16:
        return "impossible"
    if p < 1 or p > n:
        return "impossible"
    if len(set(palettes)) != p:
        return "impossible"
    for i in palettes:
        if i < 1 or i > n:
            return "impossible"
    
    # Initialize the color code with the first element
    color_code = [0] * 2**n
    color_code[0] = [0] * n
    
    # Fill in the remaining elements of the color code
    for i in range(1, 2**n):
        # Find the index of the previous element in the color code
        prev_index = (i - 1) // palettes[i % p]
        
        # Flip the bits of the previous element according to the palette
        flipped_bits = []
        for j in range(n):
            if j % palettes[i % p] == 0:
                flipped_bits.append(1 - color_code[prev_index][j])
            else:
                flipped_bits.append(color_code[prev_index][j])
        
        # Add the flipped bits to the color code
        color_code[i] = flipped_bits
    
    # Return the color code
    return "\n".join(["".join(map(str, row)) for row in color_code])

