
def solve(s, n):
    # Convert the input string to a list of characters
    chars = list(s)
    # Loop through the list of characters
    for i in range(len(chars)):
        # Calculate the new index of the character based on the shift value
        new_index = (ord(chars[i]) - ord('A') + n) % 26
        # Update the character at the new index
        chars[i] = chr(ord('A') + new_index)
    # Join the list of characters back into a string
    return "".join(chars)

