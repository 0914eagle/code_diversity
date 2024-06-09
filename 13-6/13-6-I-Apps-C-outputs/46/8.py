
def get_color_code(n, p, palettes):
    # Initialize an empty code
    code = []

    # Check if the palette is valid
    if len(set(palettes)) != len(palettes):
        return "impossible"

    # Check if the palette is too large
    if max(palettes) > n:
        return "impossible"

    # Iterate through all possible codes
    for i in range(2**n):
        # Convert the current number to binary
        binary = bin(i)[2:]

        # Pad the binary string with zeros
        binary = binary.zfill(n)

        # Check if the current code is valid
        valid = True
        for j in range(n-1):
            # Get the Hamming distance between the current and next number
            dist = hamming_distance(binary[j:j+2], binary[j+1:j+3])

            # Check if the distance is in the palette
            if dist not in palettes:
                valid = False
                break

        # If the code is valid, add it to the code
        if valid:
            code.append(binary)

    # Return the code
    return code

# Function to calculate the Hamming distance between two binary strings
def hamming_distance(s1, s2):
    # Initialize the distance
    dist = 0

    # Loop through the characters of the strings
    for c1, c2 in zip(s1, s2):
        # Check if the characters are different
        if c1 != c2:
            dist += 1

    # Return the distance
    return dist

