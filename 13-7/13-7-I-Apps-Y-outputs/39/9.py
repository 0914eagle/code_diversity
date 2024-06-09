
def solve(s, n):
    # Convert input string to uppercase
    s = s.upper()

    # Create a new string to store the result
    result = ""

    # Iterate through each character in the input string
    for c in s:
        # Calculate the shifted character position in the alphabet
        pos = (ord(c) - ord("A") + n) % 26

        # Add the shifted character to the result string
        result += chr(ord("A") + pos)

    # Return the result string
    return result

