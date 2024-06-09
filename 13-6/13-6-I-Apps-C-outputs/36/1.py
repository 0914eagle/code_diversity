
def decrypt_message(encrypted_message, fragment):
    # Initialize a dictionary to store the number of occurrences of each letter in the fragment
    letter_counts = {}
    for letter in fragment:
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1

    # Initialize a variable to store the number of positions in the encrypted message where the fragment could occur
    num_positions = 0

    # Iterate through the encrypted message
    for i in range(len(encrypted_message)):
        # Check if the letter at the current position in the encrypted message is in the fragment
        if encrypted_message[i] in letter_counts:
            # If the letter is in the fragment, decrement the count for that letter in the dictionary
            letter_counts[encrypted_message[i]] -= 1

            # If the count for the letter is 0, it means that the letter has been found in the fragment and can be removed from the dictionary
            if letter_counts[encrypted_message[i]] == 0:
                del letter_counts[encrypted_message[i]]

            # Increment the number of positions in the encrypted message where the fragment could occur
            num_positions += 1

    # If the dictionary is empty, it means that all letters in the fragment have been found in the encrypted message and the fragment is a part of the encrypted message
    if not letter_counts:
        return encrypted_message[i-num_positions+1:i+1]
    else:
        return num_positions

