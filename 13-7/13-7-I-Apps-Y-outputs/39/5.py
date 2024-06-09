
def solve(s, n):
    # Convert input string to uppercase
    s = s.upper()

    # Create a list to store the shifted characters
    shifted_chars = []

    # Loop through each character in the input string
    for char in s:
        # Calculate the shifted character by adding the shift value to the ASCII code of the character
        shifted_char = chr(ord(char) + n)

        # If the shifted character is greater than 'Z', wrap it around to 'A'
        if shifted_char > 'Z':
            shifted_char = chr(ord('A') + (ord(shifted_char) - ord('Z')))

        # Add the shifted character to the list
        shifted_chars.append(shifted_char)

    # Join the list of shifted characters into a string and return it
    return "".join(shifted_chars)

