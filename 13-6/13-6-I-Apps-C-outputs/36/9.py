
def solve(encrypted_message, fragment):
    # Initialize a dictionary to store the frequency of each letter in the fragment
    fragment_freq = {}
    for letter in fragment:
        if letter not in fragment_freq:
            fragment_freq[letter] = 1
        else:
            fragment_freq[letter] += 1

    # Initialize a variable to store the number of positions where the fragment could occur
    num_positions = 0

    # Iterate through the encrypted message
    for i in range(len(encrypted_message)):
        # If the letter at the current position is in the fragment, increment the number of positions
        if encrypted_message[i] in fragment_freq:
            num_positions += 1

    # If there is only one position where the fragment could occur, return the substring of the encrypted message that could correspond to the fragment
    if num_positions == 1:
        return encrypted_message[i-len(fragment)+1:i+1]
    # Otherwise, return the number of positions where the fragment could occur
    else:
        return num_positions

