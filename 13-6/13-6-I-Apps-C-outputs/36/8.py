
def solve(encrypted_message, decrypted_fragment):
    # Initialize a dictionary to store the number of occurrences of each letter in the decrypted fragment
    fragment_dict = {}
    for letter in decrypted_fragment:
        if letter not in fragment_dict:
            fragment_dict[letter] = 1
        else:
            fragment_dict[letter] += 1

    # Initialize a variable to store the number of positions in the encrypted message where the fragment could occur
    num_positions = 0

    # Iterate through the encrypted message
    for i in range(len(encrypted_message)):
        # If the letter at the current position in the encrypted message is in the decrypted fragment, increment the number of positions
        if encrypted_message[i] in fragment_dict:
            num_positions += 1

    # If there is only one position in the encrypted message where the fragment could occur, return the substring of the encrypted message that could correspond to the fragment
    if num_positions == 1:
        return encrypted_message[i]
    # Otherwise, return the number of positions in the encrypted message where the fragment could occur
    else:
        return num_positions

