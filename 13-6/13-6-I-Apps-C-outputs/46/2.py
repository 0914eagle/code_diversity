
def get_color_code(n, p, palete):
    # Create a list to store the color code
    color_code = []

    # Check if the palette is valid
    if len(set(palete)) != len(palete):
        return "impossible"

    # Check if the palette is greater than the number of bits
    if max(palete) > n:
        return "impossible"

    # Initialize the first string with all zeros
    current_string = [0] * n

    # Add the first string to the color code
    color_code.append("".join(map(str, current_string)))

    # Iterate through the remaining strings
    for i in range(1, 2**n):
        # Find the index of the bit that needs to be flipped
        bit_index = palete.index(i)

        # Flip the bit at the found index
        current_string[bit_index] = 1 - current_string[bit_index]

        # Add the modified string to the color code
        color_code.append("".join(map(str, current_string)))

    # Return the color code
    return color_code

