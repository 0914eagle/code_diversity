
def decrypt_message(encrypted_message, fragment):
    # Initialize a dictionary to map each letter to its corresponding position in the alphabet
    alphabet = {chr(i): i - 97 for i in range(97, 123)}

    # Initialize a list to store the positions where the fragment could occur in the encrypted message
    positions = []

    # Loop through each letter in the encrypted message
    for i, letter in enumerate(encrypted_message):
        # If the letter is in the fragment, add its position to the list of positions
        if letter in fragment:
            positions.append(i)

    # If there is only one position where the fragment could occur, return the substring of the encrypted message that could correspond to the fragment
    if len(positions) == 1:
        return encrypted_message[positions[0]:positions[0] + len(fragment)]
    # Otherwise, return the number of positions where the fragment could occur
    else:
        return len(positions)

