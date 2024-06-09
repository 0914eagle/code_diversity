
def solve(encrypted_message, decrypted_fragment):
    # Initialize a dictionary to store the frequency of each letter in the decrypted fragment
    fragment_freq = {}
    for letter in decrypted_fragment:
        if letter not in fragment_freq:
            fragment_freq[letter] = 1
        else:
            fragment_freq[letter] += 1

    # Initialize a variable to store the number of positions in the encrypted message where the fragment could occur
    num_positions = 0

    # Iterate through the encrypted message
    for i in range(len(encrypted_message)):
        # Check if the letter at the current position in the encrypted message is in the decrypted fragment
        if encrypted_message[i] in fragment_freq:
            # Increment the number of positions where the fragment could occur
            num_positions += 1

            # If the number of positions is 1, return the substring of the encrypted message that could correspond to the fragment
            if num_positions == 1:
                return encrypted_message[i:i+len(decrypted_fragment)]

    # If the number of positions is greater than 1, return the number of positions
    return num_positions

